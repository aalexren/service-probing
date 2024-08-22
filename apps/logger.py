import functools
from datetime import datetime as dt

from .generic import LoggerClient, Path


class Logger(LoggerClient):
    def __init__(self, file: Path, verbose: bool = False):
        self._file = file
        self._verbose = verbose

    @staticmethod
    def _timestamp(func):
        @functools.wraps(func)
        def inner(self, message):
            datetime = f"{dt.now():%Y-%m-%d %H:%M:%S}"
            payload = f"[{datetime}] {message}\n"
            return func(self, payload)

        return inner

    @_timestamp
    def log_message(self, message: str):
        try:
            with open(self._file, "a", encoding="utf-8") as f:
                f.write(message)

            if self._verbose:
                print(message, end="")
        except OSError as e:
            print(e)