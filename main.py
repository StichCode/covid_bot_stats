import threading

from loguru import logger

from src.functions.send_notification import send_wrapper
from src.objects.bot import start_bot
from src.objects.scheduler import CovidScheduler


def main():
    logger.info("Start bot")
    threads = [start_bot, send_wrapper, CovidScheduler().start]
    [threading.Thread(target=thr).start() for thr in threads]


if __name__ == '__main__':
    main()
