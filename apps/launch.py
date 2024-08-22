import multiprocessing
import time

from . import bootstrap, counter 
from .generic import ServiceStatus


def start(interval: float=60.):
    try:
        with multiprocessing.Pool() as pool:
            app = bootstrap.bootstrap()
            while True:
                status = pool.apply(app.watcher.get_status)
                pool.apply_async(app.logger.log_message, [status.value])
                if status == ServiceStatus.NOK:
                    pool.apply_async(
                        app.smtp.send_email,
                        [
                            "test@localhost",
                            "simpletestemail@mail.com",
                            "Service alert!",
                            "Service is not available!",
                        ],
                    )
                time.sleep(interval)
    except KeyboardInterrupt:
        print("Goodbye!")
    finally:
        pool.close()
        pool.join()

def count(file: str="events.log"):
    counter.Counter(file).show()