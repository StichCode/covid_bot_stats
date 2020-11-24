import threading

from loguru import logger

from src.objects.bot import start_bot


def main():
    logger.info("Start bot")
    [threading.Thread(target=thr).start() for thr in [start_bot]]


if __name__ == '__main__':
    main()