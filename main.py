import os
from engine_classes import HH, SuperJob
from jobs_classes import HHVacancy, SJVacancy
from jobs_classes import get_top, sorting


def clear_files():
    os.remove(f'resultHH.json')
    os.remove(f'resultSJ.json')


if __name__ == '__main__':
    print("Введите число сайта с которым хотите работать")
    vvod = int(input(' 1 : https://hh.ru/, 2 : https://api.superjob.ru/'))
    vvod_word = input("Введите ключевое слово для поиска :")
    vvod_vacancies_count = int(input('Сколько нужно вывести вакакнсий ?'))
    vvod_sort = input('Хотите отсортировать вакансии ? [Yes/No]').title()
    while True:
        search_word = vvod_word
        count = vvod_vacancies_count
        vacancies_count = 100
        if vvod == 1:
            hh_engin = HH()

            resultHH = hh_engin.get_request(search_word, vacancies_count)
            a = HH.get_connector('resultHH.json')
            a.insert(resultHH)
            HHVacancy.instantiate_from_json('resultHH.json')
            if vvod_sort == 'No':
                get_top(HHVacancy.vacancies, count)
                print(HHVacancy.get_count_of_vacancy)
            else:
                sort_list = sorting(HHVacancy.vacancies)
                get_top(sort_list, count)
                print(HHVacancy.get_count_of_vacancy)

        if vvod == 2:
            sj_engin = SuperJob()
            resultSJ = sj_engin.get_request(search_word, vacancies_count)
            b = SuperJob.get_connector('resultSJ.json')
            b.insert(resultSJ)
            SJVacancy.instantiate_from_json('resultSJ.json')
            if vvod_sort == 'No':
                get_top(SJVacancy.vacancies, count)
                print(SJVacancy.get_count_of_vacancy)
            else:
                sort_list = sorting(SJVacancy.vacancies)
                get_top(sort_list, count)
                print(SJVacancy.get_count_of_vacancy)

        clear_files()
        break
