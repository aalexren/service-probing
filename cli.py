import functools

import fire
from dotenv import load_dotenv

from apps import launch

if __name__ == "__main__":
    load_dotenv()

    fire.Fire(
        {
            "run": functools.partial(launch.start, 60.),
            "log:read": functools.partial(launch.count, "events.log")
        }
    )
