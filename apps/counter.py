from collections import defaultdict

from .generic import Path


class Counter:
    def __init__(self, file: Path):
        self._file = file

    def _count_nok(self) -> dict[str, int]:
        counter = defaultdict(lambda: 0)
        with open(self._file, "r", encoding="utf-8") as f:
            for line in f:
                if line.rfind("NOK") >= 0:
                    counter[self._get_label_from_log_line(line)] += 1
        return counter

    def show(self):
        print(f"NOK count by every hour in {self._file} file")
        result = self._count_nok()
        for k, v in sorted(result.items()):
            print(f"{k}: {v}")

    def _get_label_from_log_line(self, line: str):
        date, time, _ = line.split()
        date = date.strip("[]")
        time = time.strip("[]")
        h, m, s = time.split(":")  # hours, minutes, seconds
        return h
