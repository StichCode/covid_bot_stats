import os


class Config(object):
    TOKEN = os.getenv("TOKEN")
    PROXY_USERNAME = os.getenv("PROXY_USERNAME")
    PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")
    PROXY_ADDRESS = os.getenv("PROXY_ADDRESS")
    PROXY_PORT = os.getenv("PROXY_PORT")