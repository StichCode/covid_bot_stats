from queue import Queue

import requests
from loguru import logger

from config import CONFIG
from src.objects.construct_url import Url


NOTIFY_QUEUE = Queue()
URL = Url()


def send_wrapper():
    logger.info("Start thread for sending messages from queue")
    while True:
        item = NOTIFY_QUEUE.get()
        logger.info("Get data from queue")
        for user in CONFIG.users:
            __send(user_id=user, text=item)
        NOTIFY_QUEUE.task_done()


def __send(user_id: int, text: str):
    headers = {"Content-Type": "application/json"}
    data = {"chat_id": user_id, "text": text}
    logger.info("Try send message to user: {} \n {}".format(data['chat_id'], data["text"]))
    try:
        requests.post(url=URL.send_text, headers=headers, data=data)
        logger.info("Successfully send message")
    except Exception as ex:
        logger.exception("Message not send with exception")
        logger.exception(ex)
