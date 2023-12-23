from classes.hh_api_class import HeadHunterAPI
from classes.saver_class import JSONSaver
from classes.superjob_api_class import SuperJobAPI
from src.utils import (get_sj_vacancies_instances,
                       get_hh_vacancies_instances,
                       convert_instances_to_json,
                       sort_vacancies_by_date,
                       sort_vacancies_by_salary)
from pprint import pprint


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("""Введите поисковый запрос:
    ->>> """)
    platforms = int(input("""Введите желаемые поисковые сайты:
        0 - HeadHunter и SuperJob;
        1 - только HeadHunter;
        2 - только SuperJob;
    ->>> """))

    if platforms == 0:
        # Создание экземпляра класса для работы с API сайтов с вакансиями
        hh_api = HeadHunterAPI()
        superjob_api = SuperJobAPI()
        # Получение вакансий с разных платформ
        hh_vacancies = hh_api.get_vacancies(search_query)
        superjob_vacancies = superjob_api.get_vacancies(search_query)
        # Создание экземпляров класса для работы с вакансиями
        list_all_instances = get_hh_vacancies_instances(hh_vacancies) + get_sj_vacancies_instances(superjob_vacancies)

    elif platforms == 1:
        hh_api = HeadHunterAPI()  # Создание экземпляра класса для работы с API HH
        hh_vacancies = hh_api.get_vacancies(search_query)  # Получение вакансий с HH
        # Создание экземпляров класса для работы с вакансиями
        list_all_instances = get_hh_vacancies_instances(hh_vacancies)

    elif platforms == 2:
        superjob_api = SuperJobAPI()  # Создание экземпляра класса для работы с API SJ
        superjob_vacancies = superjob_api.get_vacancies(search_query)  # Получение вакансий с SJ
        # Создание экземпляров класса для работы с вакансиями
        list_all_instances = get_sj_vacancies_instances(superjob_vacancies)

    else:
        print("Неверно, запустите заново.")
        return

    if not list_all_instances:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    # Преобразование списка экземпляров класса Vacancy в json формат
    vacancies_json_list = convert_instances_to_json(list_all_instances)
    print(f"Найдено {len(vacancies_json_list)} вакансий.")

    # Сохранение списка вакансий в файл
    json_saver = JSONSaver()
    json_saver.add_vacancies(vacancies_json_list)

    output_choice = int(input("""Введите желаемый вариант вывода:
    1 - Для вывода всех вакансий отфильтрованных по дате;
    2 - Для вывода всех вакансий отфильтрованных по зарплате;
    3 - Для выбора топ # вакансий по дате;
    4 - Для вывода топ # вакансий по зарплате;
    5 - Для вывода топ # вакансий по зарплате и по дате;
    ->>> """))

    if output_choice == 1:
        pprint(sort_vacancies_by_date(vacancies_json_list))
    elif output_choice == 2:
        pprint(sort_vacancies_by_salary(vacancies_json_list))
    elif output_choice == 3:
        y = int(input("Введите количество вакансий для вывода "))
        pprint(sort_vacancies_by_date(vacancies_json_list)[:y])
    elif output_choice == 4:
        x = input("Введите нижний и верхний порог через пробел ")
        from_ = int(x.split(" ")[0])
        to_ = int(x.split(" ")[1])
        choisen_vacancies = json_saver.get_vacancies_by_salary(from_, to_)
        y = int(input("Введите количество вакансий для вывода "))
        pprint(sort_vacancies_by_salary(choisen_vacancies)[:y])
    elif output_choice == 5:
        x = input("Введите нижний и верхний порог через пробел ")
        from_ = int(x.split(" ")[0])
        to_ = int(x.split(" ")[1])
        choisen_vacancies = json_saver.get_vacancies_by_salary(from_, to_)
        y = int(input("Введите количество вакансий для вывода "))
        pprint(sort_vacancies_by_date(choisen_vacancies)[:y])
    else:
        print("Неверно, запустите заново.")
        # json_saver.delete_vacancies()
        return

    # json_saver.delete_vacancies()


user_interaction()
