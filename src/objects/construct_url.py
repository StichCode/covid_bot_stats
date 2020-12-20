from config import CONFIG


class Url:
    def __init__(self):
        self._host = "api.telegram.org"
        self._token = CONFIG.token

    @property
    def _url(self):
        return "https://{0}/bot{1}".format(self._host, self._token)

    def send_text(self, chat_id, text, parse_mod="markdown"):
        return '{0}/sendMessage?chat_id={1}&text={2}&parse_mode='.format(self._url, chat_id, text, parse_mod)

    def error_message(self, text):
        return self.send_text(295290188, text)
