import requests

from .generic import ServiceStatus, WatcherClient


class ProbingClient(WatcherClient):
    def __init__(self, url: str):
        self._url = url

    def get_status(self, **extra) -> ServiceStatus | None:
        try:
            with requests.Session() as s:
                response = s.get(self._url, **extra)
            code = response.status_code
            return ServiceStatus.OK if code < 500 else ServiceStatus.NOK
        except requests.exceptions.RequestException as e:
            print(f"Error has occured: {e}")
        return None


# import httpx
# import asyncio
# from datetime import datetime
# from functools import partial


# def log_event(msg):
#     with open("events.log", "+a") as f:
#         f.write(msg)

# async def check_url():
#     async with httpx.AsyncClient() as client:
#         response = await client.get("http://example.com", follow_redirects=False)
#         print(response.status_code)
#         return response.status_code

# async def main():
#     while True:
#         result = await asyncio.create_task(check_url())
#         await asyncio.to_thread(
#             partial(log_event, f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {result}\n")
#         )
#         await asyncio.sleep(2)


# asyncio.run(main())
