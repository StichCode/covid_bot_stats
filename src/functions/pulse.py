from threading import Thread
from typing import List

from loguru import logger


def pulse_thread(threads: List[Thread]) -> None:
    for thread in threads:
        message = "{0} is alive! ♥ \n" if thread.is_alive() else "{0} is die! (×_×)\n"
        logger.info(message.format(thread.name))
