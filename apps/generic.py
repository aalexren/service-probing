import enum
from typing import Protocol


class EmailClient(Protocol):
    def send_email(
        self,
        from_email: str,
        to_email: str,
        subject: str,
        message: str,
        login: str | None = None,
        password: str | None = None,
    ): ...


class LoggerClient(Protocol):
    def log_message(self, message: str): ...


class WatcherClient(Protocol):
    def get_status(self, **extra): ...


class App:
    smtp: EmailClient
    logger: LoggerClient
    watcher: WatcherClient


Path = str


class ServiceStatus(str, enum.Enum):
    OK = "OK"
    NOK = "NOK"
