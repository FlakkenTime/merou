from collections import namedtuple
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text

from grouper.constants import MAX_NAME_LENGTH
from grouper.models.base.model_base import Model

MappedPermission = namedtuple(
    "MappedPermission", ["permission", "audited", "argument", "groupname", "granted_on", "alias"]
)


class Permission(Model):
    """
    Represents permission types. See PermissionEdge for the mapping of which permissions
    exist on a given Group.
    """

    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)

    name = Column(String(length=MAX_NAME_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow, nullable=False)
    _audited = Column("audited", Boolean, default=False, nullable=False)
    enabled = Column("enabled", Boolean, default=True, nullable=False)

    @staticmethod
    def get(session, name=None):
        if name is not None:
            return session.query(Permission).filter_by(name=name).scalar()
        return None

    @property
    def audited(self):
        return self._audited
