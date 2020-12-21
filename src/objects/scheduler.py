from copy import copy
from time import time

from loguru import logger

from src.functions.send_notification import NOTIFY_QUEUE
from src.objects.cache import CACHE
from src.objects.covid19_statistic import CovidStats


class CovidScheduler:
    """ Каждый час кладёт статистику если изменилась """

    def __init__(self) -> None:
        self.covid = CovidStats
        self.prev_data = ""

    def check(self) -> None:
        parser = self.covid()
        self.caching(parser)
        data = parser.html()
        if self.prev_data != data:
            logger.info("Put data to queue > {}".format(data))
            NOTIFY_QUEUE.put(data)
            self.prev_data = copy(data)
        else:
            logger.info("No new data")

    @staticmethod
    def caching(parser) -> None:
        logger.info("start caching statistic")
        general, russia = parser.html(), parser.html('location')
        CACHE.put_statistic(int(time()), russia, False)
        CACHE.put_statistic(int(time()), general, True)
        logger.info("complete")
