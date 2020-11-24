from copy import copy

import schedule
from loguru import logger

from src.functions.send_notification import NOTIFY_QUEUE
from src.objects.covid19_statistic import CovidStats


class CovidScheduler:
    """ Каждый час кладёт статистику если изменилась """

    def __init__(self):
        self.covid = CovidStats
        self.prev_data = ""

    def __check_data(self):
        data = self.covid().html()
        if self.prev_data != data:
            logger.info("Put data to queue > {}".format(data))
            NOTIFY_QUEUE.put(data)
            self.prev_data = copy(data)
        else:
            logger.info("No new data")

    def start(self):
        logger.info("Start thread with scheduler")
        schedule.every(interval=12).hours.do(self.__check_data)
        while True:
            schedule.run_pending()
