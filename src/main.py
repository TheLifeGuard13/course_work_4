from pprint import pprint

from classes.hh_api_class import HeadHunterAPI
from classes.saver_class import JSONSaver
from classes.superjob_api_class import SuperJobAPI
from src.utils import (
    convert_instances_to_json,
    get_hh_vacancies_instances,
    get_sj_vacancies_instances,
    sort_vacancies_by_date,
    sort_vacancies_by_salary,
)


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    search_query = input(
        """Введите поисковый запрос:
    (для уточнения, запрос может содержать более одного слова - вводятся через пробел)
    ->>> """
    )
    platforms = input(
        """Введите желаемые поисковые сайты:
        h - только HeadHunter;
        s - только SuperJob;
        По умолчанию - HeadHunter и SuperJob;
    ->>> """
    )
    try:
        if platforms.lower() == "h":
            hh_api = HeadHunterAPI()  # Создание экземпляра класса для работы с API HH
            hh_vacancies = hh_api.get_vacancies(search_query)  # Получение вакансий с HH
            # Создание экземпляров класса для работы с вакансиями
            all_instances_list = get_hh_vacancies_instances(hh_vacancies)

        elif platforms.lower() == "s":
            superjob_api = SuperJobAPI()  # Создание экземпляра класса для работы с API SJ
            superjob_vacancies = superjob_api.get_vacancies(search_query)  # Получение вакансий с SJ
            # Создание экземпляров класса для работы с вакансиями
            all_instances_list = get_sj_vacancies_instances(superjob_vacancies)

        else:
            # Создание экземпляра класса для работы с API сайтов с вакансиями
            hh_api = HeadHunterAPI()
            superjob_api = SuperJobAPI()
            # Получение вакансий с разных платформ
            hh_vacancies = hh_api.get_vacancies(search_query)
            superjob_vacancies = superjob_api.get_vacancies(search_query)
            # Создание экземпляров класса для работы с вакансиями
            all_instances_list = get_hh_vacancies_instances(hh_vacancies) + get_sj_vacancies_instances(
                superjob_vacancies
            )
    except Exception:
        raise Exception

    if not all_instances_list:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    # Преобразование списка экземпляров класса Vacancy в json формат
    vacancies_json_list = convert_instances_to_json(all_instances_list)
    print(f"Найдено {len(vacancies_json_list)} вакансий.")

    # Сохранение списка вакансий в файл
    json_saver = JSONSaver()
    json_saver.add_vacancies(vacancies_json_list)

    output_choice = input(
        """Введите желаемый вариант вывода:
    d - Для вывода топ # вакансий по дате;
    s - Для вывода топ # вакансий по зарплате;
    sd - Для вывода топ # вакансий по зарплате и по дате;
    По умолчанию - вывод всех вакансий отфильтрованных по дате
    ->>> """
    )

    if output_choice.lower() == "d":
        user_number_input = input("Введите количество вакансий для вывода ")
        try:
            pprint(sort_vacancies_by_date(vacancies_json_list)[: int(user_number_input)])
        except ValueError:
            print("Ошибка ввода")
            return

    elif output_choice.lower() == "s":
        try:
            salary_input = input("Введите нижний и верхний порог зарплаты через пробел ")
            from_ = salary_input.split(" ")[0]
            to_ = salary_input.split(" ")[1]
            choisen_vacancies = json_saver.get_vacancies_by_salary(int(from_), int(to_))
            user_number_input = input("Введите количество вакансий для вывода ")
            pprint(sort_vacancies_by_salary(choisen_vacancies)[: int(user_number_input)])
        except ValueError:
            print("Ошибка ввода")
            return

    elif output_choice.lower() == "sd":
        try:
            salary_input = input("Введите нижний и верхний порог зарплаты через пробел ")
            from_ = salary_input.split(" ")[0]
            to_ = salary_input.split(" ")[1]
            choisen_vacancies = json_saver.get_vacancies_by_salary(int(from_), int(to_))
            user_number_input = input("Введите количество вакансий для вывода ")
            pprint(sort_vacancies_by_date(choisen_vacancies)[: int(user_number_input)])
        except ValueError:
            print("Ошибка ввода")
            return

    else:
        pprint(sort_vacancies_by_date(vacancies_json_list))


user_interaction()
