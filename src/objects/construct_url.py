from config import CONFIG


class Url:
    def __init__(self):
        self._host = "api.telegram.org"
        self._token = CONFIG.token

    @property
    def _url(self):
        return "https://{0}/bot{1}".format(self._host, self._token)

    @property
    def send_text(self):
        return '{0}/{1}'.format(self._url, "sendMessage")
