from copy import copy
from loguru import logger

from src.functions.send_notification import NOTIFY_QUEUE
from src.objects.covid19_statistic import CovidStats


class CovidScheduler:
    """ Каждый час кладёт статистику если изменилась """

    def __init__(self):
        self.covid = CovidStats
        self.prev_data = ""

    def check(self):
        data = self.covid().html()
        if self.prev_data != data:
            logger.info("Put data to queue > {}".format(data))
            NOTIFY_QUEUE.put(data)
            self.prev_data = copy(data)
        else:
            logger.info("No new data")
