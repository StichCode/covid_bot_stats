from typing import Optional

import requests
from bs4 import BeautifulSoup
from loguru import logger

from config import CONFIG
from src.functions.prepare_data import convert_to_html


class CovidStats:

    def __init__(self) -> None:
        self.url = CONFIG.url
        self.bs = BeautifulSoup(requests.get(self.url).content, 'html.parser')
        self.table_tag = self.bs.table

    def get_all_stats(self) -> dict:
        stats = self.bs.find_all("div", attrs={"id": "maincounter-wrap"})
        dict_with_stats = {}
        for div in stats:
            dict_with_stats[div.h1.string[:-1]] = div.div.span.string
        logger.debug("Get global stats")
        return dict_with_stats

    def get_stats_by_location(self, country_code="Russia") -> dict:
        data = self.__prepare_data()
        return data[country_code]

    def get_all_countries(self):
        tbody = self.table_tag.tbody.find_all("tr")
        result_list = []
        for i in range(len(tbody)):
            result_list.append(tbody[i].find_all("td")[0].string)
        return result_list

    def __get_data(self) -> list:
        tbody = self.table_tag.tbody.find_all("tr")
        result = []
        for i in range(len(tbody)):
            result.append([td.string for td in tbody[i].find_all("td")])
        logger.debug("Get data from WorldMeters")
        return result

    def __prepare_data(self) -> dict:
        data = self.__get_data()
        new_prepared_dict = {}
        for row in data:
            if row[0] is None:
                continue
            new_prepared_dict[row[1]] = dict([i for i in zip(CONFIG.thead, row)])
        logger.debug("Prepared data complete")
        return new_prepared_dict

    def html(self, name_data: Optional[str] = None):
        data = self.get_all_stats()
        if name_data == "location":
            data = self.get_stats_by_location()
        return convert_to_html(data)
