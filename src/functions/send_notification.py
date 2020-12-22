from queue import Queue

import requests
from loguru import logger

from config import CONFIG
from src.objects.cache import CACHE
from src.objects.construct_url import Url


NOTIFY_QUEUE = Queue()
URL = Url()


def send_wrapper():
    logger.info("Start thread for sending messages from queue")
    while True:
        item = NOTIFY_QUEUE.get()
        logger.info("Get data from queue")
        for user in CACHE.notify_users_id():
            __send(user_id=user[0], text=item)
        NOTIFY_QUEUE.task_done()


def __send(user_id: int, text: str):
    headers = {"Content-Type": "application/json"}
    url = URL.send_text(user_id, text, parse_mod='html')
    logger.info("Try send message to url: {}".format(url))
    try:
        res = requests.post(url=url, headers=headers)
        if res.status_code != 200:
            raise Exception(f"Status code: {res.status_code}")
        logger.info("Successfully send message")
    except Exception:
        logger.exception("Message not send")
