import os
from typing import List

from loguru import logger
from pydantic import BaseModel


class Config(BaseModel):
    token: str
    url: str
    thead: List[str]
    admins: List[int]


CONFIG = Config(
    token=os.getenv("TOKEN"),
    url="https://www.worldometers.info/coronavirus/",
    thead=['Num',
           'Country',
           'Total cases',
           'New Cases',
           'Total Deaths',
           'New Deaths',
           'Total Recovered',
           'New Recovered',
           'Active Cases',
           'Critical'],
    admins=[295290188],
)

logger.info(CONFIG)
