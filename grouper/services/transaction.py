from contextlib import contextmanager
from typing import TYPE_CHECKING

from grouper.repositories.transaction import TransactionRepository
from grouper.usecases.interfaces import TransactionInterface

if TYPE_CHECKING:
    from grouper.repositories.checkpoint import CheckpointRepository
    from typing import Iterator


class TransactionService(TransactionInterface):
    """Manage storage layer transactions encompassing multiple service actions."""

    def __init__(self, transaction_repository, checkpoint_repository):
        # type: (TransactionRepository, CheckpointRepository) -> None
        self.transaction_repository = transaction_repository
        self.checkpoint_repository = checkpoint_repository

    def commit(self):
        # type: () -> None
        """Provided for tests, do not use in use cases."""
        self.checkpoint_repository.update_checkpoint()
        self.transaction_repository.commit()

    @contextmanager
    def transaction(self):
        # type: () -> Iterator[None]
        with self.transaction_repository.transaction():
            yield
            self.checkpoint_repository.update_checkpoint()
