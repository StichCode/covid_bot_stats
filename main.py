import threading

from loguru import logger

from src.functions.pulse import pulse_thread
from src.functions.send_notification import send_wrapper
from src.objects.bot import start_bot
from src.objects.construct_url import Url
from src.objects.interval import Interval
from src.objects.scheduler import CovidScheduler


def main():
    logger.add("file.log")
    logger.info("Start bot")
    threads_names = {start_bot: "BotThread", send_wrapper: "NotifyThread"}
    interval = Interval(interval=1800, function=CovidScheduler().check)  # every 1 hour
    interval.name = "IntervalThread"
    interval.start()

    threads = [threading.Thread(target=thr, name=name)for thr, name in threads_names.items()]
    [thr.start() for thr in threads]

    threads.append(interval)

    pulse = Interval(interval=10, function=pulse_thread, args=(threads,))
    pulse.daemon = True
    pulse.start()


if __name__ == '__main__':
    main()
