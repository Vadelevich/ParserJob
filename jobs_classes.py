import json
from abc import ABC, abstractmethod


class AbstractObject(ABC):
    """ Абстрактный метод для преопределения функции  instantiate_from_json в дочерних классах """
    @abstractmethod
    def instantiate_from_json(self):
        raise NotImplementedError("Please Implement this method")


class Vacancy:
    name_class = 'Vacancy'
    __slots__ = ('name', 'hrep', 'salary')

    def __init__(self, name, hrep, salary):
        self.name = name
        self.hrep = hrep
        self.salary = salary

    def __str__(self):
        a = 'не указана'
        return f'{self.name_class} : {self.comany_name}, зарплата: {self.salary if self.salary else a} руб/мес'

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __iter__(self):
        self.value = 0
        return self.value

    def __next__(self):
        if self.value < len(self.vacancies):
            self.value += 1
        else:
            raise StopIteration


class CountMixin:
    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        with open(self.file, 'r') as f:
            my_file = json.load(f)
            for i in my_file:
                for item in i:
                    self.count += 1
        return self.count


class HHVacancy(Vacancy, CountMixin, AbstractObject):  # add counter mixin
    """ HeadHunter Vacancy """
    vacancies = []
    name_class = "HH"
    file = 'resultHH.json'

    def __init__(self, name, hrep, salary, company_name):
        super().__init__(name, hrep, salary)
        self.comany_name = company_name
        self.name_class = HHVacancy.name_class
        self.count = CountMixin.get_count_of_vacancy

    @classmethod
    def instantiate_from_json(cls, file):
        with open(f'{file}') as f:
            file_opened = json.load(f)
            for i in file_opened:
                for item in i:
                    a = item.get('name')
                    b = item.get('url')
                    try:
                        c = item.get('salary').get('from')
                        if c == None: c = 0
                    except AttributeError:
                        c = 0
                    comany_name = item.get("employer").get('name')

                    cls.vacancies.append(HHVacancy(a, b, c, comany_name))


class SJVacancy(Vacancy, CountMixin, AbstractObject):  # add counter mixin
    """ SuperJob Vacancy """
    vacancies = []
    name_class = "SJ"
    file = 'resultSJ.json'

    def __init__(self, name, hrep, salary, company_name):
        super().__init__(name, hrep, salary)
        self.comany_name = company_name
        self.name_class = SJVacancy.name_class
        self.file = SJVacancy.file

    @classmethod
    def instantiate_from_json(cls, file):
        with open(f'{file}') as f:
            file_opened = json.load(f)
            for i in file_opened:
                for item in i:
                    a = item.get("profession")
                    b = item.get("link")
                    try:
                        c = item.get("payment_from")
                        if c == None: c = 0
                    except AttributeError:
                        c = 0

                    comany_name = item.get("firm_name")

                    cls.vacancies.append(SJVacancy(a, b, c, comany_name))


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    vacancies = sorted(vacancies, reverse=True)
    return vacancies


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    try:
        for i in range(top_count):
            print(vacancies[i])
    except IndexError:
        print(f'{top_count} вакансий нет! Это все что есть ')


if __name__ == '__main__':
    SJVacancy.instantiate_from_json('resultSJ.json')
    sort_list = sorting(SJVacancy.vacancies)
    get_top(sort_list, 204555)
    HHVacancy.instantiate_from_json('resultHH.json')
    sort_list = sorting(HHVacancy.vacancies)
    get_top(sort_list, 2100)

    print(HHVacancy.get_count_of_vacancy)
