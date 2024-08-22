import os

from .generic import App, Path
from .logger import Logger
from .smtp import SMTPClient
from .watcher import ProbingClient


def _bootstrap_smtp(host: str, port: int, **extra):
    client = SMTPClient(host, port, **extra)
    return client


def _bootstrap_logger(file: Path, verbose: bool = True):
    client = Logger(file, verbose)
    return client


def _bootstrap_watcher(url: str):
    client = ProbingClient(url)
    return client


def bootstrap():
    # configs for clients would be nice
    app = App()

    app.smtp = _bootstrap_smtp(
        os.environ.get("SMTP_HOST", "smtp.freesmtpservers.com"),
        int(os.environ.get("SMTP_PORT", 25)),
        timeout=int(os.environ.get("SMTP_TIMEOUT", 10)),
    )
    app.logger = _bootstrap_logger(
        os.environ.get("LOG_FILE", "events.log"),
        bool(os.environ.get("LOG_VERBOSE", True)),
    )
    app.watcher = _bootstrap_watcher(
        os.environ.get("WATCHER_URL", "http://example.com")
    )

    return app
