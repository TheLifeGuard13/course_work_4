from classes.vacancies_class import Vacancy
from datetime import datetime


def get_hh_vacancies_instances(vacancies: list[dict]) -> list[Vacancy]:
    """
    Инициализирует полученные вакансии HeadHunter в экземпляры Класса Vacancy
    """
    list_ = []
    if not vacancies:
        return []
    for vacancy in vacancies:
        list_.append(Vacancy(vacancy_id=vacancy["id"],
                             vacancy_url=vacancy["alternate_url"],
                             vacancy_pub_date=datetime.fromisoformat(vacancy["published_at"]).strftime("%d.%m.%Y"),
                             experience=vacancy["experience"]["name"],
                             vacancy_name=vacancy["name"],
                             salary_currency=vacancy["salary"]["currency"],
                             salary_from=vacancy["salary"]["from"],
                             salary_limit=vacancy["salary"]["to"],
                             work_schedule=vacancy["schedule"]["name"],
                             salary_status=not vacancy["salary"]["gross"]
                             )
                     )
    return list_


def get_sj_vacancies_instances(vacancies: list[dict]) -> list[Vacancy]:
    """
    Инициализирует полученные вакансии SuperJob в экземпляры Класса Vacancy
    """
    list_ = []
    if not vacancies:
        return []
    for vacancy in vacancies:
        list_.append(Vacancy(vacancy_id=vacancy["id"],
                             vacancy_url=vacancy["link"],
                             vacancy_pub_date=datetime.fromtimestamp(vacancy["date_published"]).strftime("%d.%m.%Y"),
                             experience=vacancy["experience"]["title"],
                             vacancy_name=vacancy["profession"],
                             salary_currency=vacancy["currency"],
                             salary_from=vacancy["payment_from"],
                             salary_limit=vacancy["payment_to"],
                             work_schedule=vacancy["type_of_work"]["title"],
                             salary_status=False
                             )
                     )
    return list_


def convert_instances_to_json(vacancies: list[Vacancy]) -> list[dict]:
    """
    Конвертирует список экземпляров класса Vacancy в список словарей
    """
    list_ = []
    for instance in vacancies:
        dict_ = {}
        dict_["id вакансии"] = instance.vacancy_id
        dict_["Наименование вакансии"] = instance.vacancy_name
        dict_["Ссылка"] = instance.vacancy_url
        dict_["Требуемый опыт"] = instance.experience
        dict_["Дата размещения"] = instance.vacancy_pub_date
        dict_["Зарплата от"] = instance.salary_from
        dict_["Зарплата до"] = instance.salary_limit
        dict_["Валюта"] = instance.salary_currency
        dict_["График работы"] = instance.work_schedule
        list_.append(dict_)
    return list_


def sort_vacancies_by_date(vacancies: list) -> list:
    """
    Сортирует вакансии по дате
    """
    for v in vacancies:
        v["Дата размещения"] = datetime.strptime(v["Дата размещения"], "%d.%m.%Y")
    sorted_vacancies = sorted(vacancies, key=lambda x: x["Дата размещения"], reverse=True)
    for v in sorted_vacancies:
        v["Дата размещения"] = v["Дата размещения"].strftime("%d.%m.%Y")
    return sorted_vacancies


def sort_vacancies_by_salary(vacancies: list) -> list:
    """
    Сортирует вакансии по зарплате
    """
    return sorted(vacancies, key=lambda x: x["Зарплата от"], reverse=True)
