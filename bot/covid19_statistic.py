import requests
from bs4 import BeautifulSoup


class CovidStats:
    thead = ['Country', 'Total cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases']

    previous_all_data_from_table = []

    def __init__(self):
        self.url = "https://www.worldometers.info/coronavirus/"
        self.bs = BeautifulSoup(requests.get(self.url).content, 'html.parser')
        self.table_tag = self.bs.table

    def get_all_stats(self):
        stats = self.bs.find_all("div", attrs={"id": "maincounter-wrap"})
        dict_with_stats = {}
        for div in stats:
            dict_with_stats[div.h1.string[:-1]] = div.div.span.string
        return dict_with_stats

    def __get_data(self):
        tbody = self.table_tag.tbody.find_all("tr")
        result = []
        for i in range(len(tbody)):
            result.append([td.string for td in tbody[i].find_all("td")])
        return result

    def __prepare_data(self):
        data = self.__get_data()
        new_prepared_dict = {}
        for row in data:
            new_prepared_dict[row[0]] = dict([i for i in zip(self.thead, row)])
        self.previous_all_data_from_table = new_prepared_dict
        return new_prepared_dict

    def get_stats_by_location(self, country_code="Russia"):
        data = self.__prepare_data()
        return data[country_code]

    def get_all_countries(self):
        tbody = self.table_tag.tbody.find_all("tr")
        result_list = []
        for i in range(len(tbody)):
            result_list.append(tbody[i].find_all("td")[0].string)
        return result_list

    @staticmethod
    def convert_to_html(data):
        prepare_message = "<u>Stats about Pandemic:</u>\n"
        for k, v in data.items():
            prepare_message += f"<b>{k}</b>: {v}\n"
        return prepare_message