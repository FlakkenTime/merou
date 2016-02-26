import pytz

from ..settings import Settings, settings as base_settings


class FeSettings(Settings):

    default_timezone = pytz.timezone("UTC")

    def override_timezone(self, value):
        try:
            return pytz.timezone(value)
        except pytz.exceptions.UnknownTimeZoneError:
            return self.default_timezone


settings = FeSettings.from_settings(base_settings, {
    "address": None,
    "cdnjs_prefix": "//cdnjs.cloudflare.com",
    "date_format": "%Y-%m-%d %I:%M %p",
    "debug": False,
    "how_to_get_help": None,
    "num_processes": 1,
    "port": 8989,
    "refresh_interval": 60,
    "site_docs": None,
    "timezone": FeSettings.default_timezone,
    "url": "http://127.0.0.1:8888",
    "user_auth_header": "X-Grouper-User",
})
