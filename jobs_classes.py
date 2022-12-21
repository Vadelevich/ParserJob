class Vacancy:
    __slots__ = ('name','hrep','description','salary')

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        # self.hrep = kwargs.get('url')
        # self.salary = kwargs.get('salary')
        # self.description = kwargs.get('area')


    def __str__(self):
        return f'Вакансия{self.name} в {self.description},ссылка {self.hrep} заработная плата {self.salary} '



class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass



class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'HH: {self.comany_name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.comany_name}, зарплата: {self.salary} руб/мес'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass