from apscheduler.schedulers.asyncio import AsyncIOScheduler
from time import sleep
import asyncio


class Scheduler:
    def __init__(self, sched_type=AsyncIOScheduler) -> None:
        self.scheduler = sched_type

    def run(self, func, period, args):
        loop = asyncio.get_event_loop()
        sched = self.scheduler({"event_loop": loop})
        sched.add_job(func, "interval", seconds=period, args=args, id="async_sched")
        sched.start()
        print("\nTo stop the scheduler, Press Ctrl+C.\n")

        try:
            loop.run_forever()
        except KeyboardInterrupt as err:
            print("\n\nThe scheduler has been stopped.\n")

        # while True:
        #     sleep(1)
