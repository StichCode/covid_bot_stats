import os


class Config(object):
    TOKEN = os.getenv("TOKEN")
    PROXY_USERNAME = os.getenv("PROXY_USERNAME")
    PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")
    PROXY_IP = os.getenv("PROXY_IP")
    PROXY_PORT = os.getenv("PROXY_PORT")