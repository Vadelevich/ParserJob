import json
from abc import ABC, abstractmethod
from connector import Connector

import requests


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        raise NotImplementedError("Please Implement this method")

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        df = Connector(f'{file_name}')
        return df


class HH(Engine):
    __url = 'https://api.hh.ru/'
    __per_page = 20

    def get_vacancies(self,search_word, page):
        responce = requests.get(f'{self.__url}vacancies?text={search_word} & page={page}')
        if responce.status_code == 200:
            return responce.json()
        return None

    def get_request(self, search_word, vacancies_count):
        page = 0
        result = []
        while self.__per_page * page <= vacancies_count:
            tmp_result = self.get_vacancies(search_word, page)
            if tmp_result:
                result += tmp_result.get('items')
                page += 1
            else:
                break
        return result



class SuperJob(Engine):
    __url ='https://api.superjob.ru/2.0'
    __secret = 'v3.r.137222925.e19a5b1d365a0b99989617dcad19e1cd15568674.3a6e44ce0f5c2b6e6abef59e6665ed279b5641bc'
    __per_page = 20

    def _send_request(self,search_word,page):
        url = f'{self.__url}/vacancies/?page={page}&keyword={search_word}'
        headers = {
            'X-Api-App-Id': self.__secret,
            'Content-Type':'application/x-www-form-urlencoded'
        }
        responce = requests.get(url=url,headers=headers)
        if responce.status_code == 200:
            return responce.json()
        return None

    def get_request(self,search_word,vacancies_count ):
        page = 0
        result = []
        while self.__per_page * page <= vacancies_count:
            tmp_result = self._send_request(search_word, page)
            if tmp_result:
                result += tmp_result.get('objects')
                page += 1
            else:
                break
        return result


if __name__ == '__main__':
    hh_engin = HH ()
    search_word = 'python'
    vacancies_count = 100
    resultHH = hh_engin.get_request(search_word,vacancies_count)
    a = HH.get_connector('resultHH.json')
    a.insert(resultHH)
    sj_engin = SuperJob()
    resultSJ = sj_engin.get_request(search_word,vacancies_count)
    b = SuperJob.get_connector('resultSJ.json')
    b.insert(resultSJ)

