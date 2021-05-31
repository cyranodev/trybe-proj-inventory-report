from datetime import datetime
from typing import Counter


class ReportsUtils:
    @staticmethod
    def get_oldest(content_list, key):
        oldest_date = [
            item[key] for item in content_list
        ]
        oldest_date.sort()
        return oldest_date[0]

    @staticmethod
    def get_next_to_expire(content_list):
        _current_date = datetime.now()

        _expiration_list = [
            item["data_de_validade"]
            for item in content_list
            if datetime.strptime(
                item["data_de_validade"], "%Y-%m-%d"
            ) > _current_date
        ]
        _expiration_list.sort()
        return _expiration_list[0]

    @staticmethod
    def get_stock(content_list):
        _list_companies = [item["nome_da_empresa"] for item in content_list]
        list_counter = Counter(_list_companies)
        return list_counter

    @classmethod
    def get_largest_stock(cls, content_list):
        _companies_list = cls.get_stock(content_list)
        most_common = _companies_list.most_common()[0][0]
        return str(most_common)
