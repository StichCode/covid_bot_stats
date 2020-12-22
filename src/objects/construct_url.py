from loguru import logger

from config import CONFIG


def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"Generate string =>>> {result}")
        return result
    return wrapper


class Url:
    def __init__(self):
        self._host = "api.telegram.org"
        self._token = CONFIG.token

    @property
    def _url(self):
        return "https://{0}/bot{1}".format(self._host, self._token)

    @log_result
    def send_text(self, chat_id, text, parse_mod="markdown"):
        return '{0}/sendMessage?chat_id={1}&text={2}&parse_mode={3}'.format(self._url, chat_id, text, parse_mod)

    @log_result
    def error_message(self, text):
        return self.send_text(295290188, text)
