from classes.vacancies_class import Vacancy
from datetime import datetime


def get_hh_vacancies_instances(vacancies: dict) -> list[Vacancy]:
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


def get_sj_vacancies_instances(vacancies: dict) -> list[Vacancy]:
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

# def get_executed_operations(operations: list[Operation]) -> list[Operation]:
#     return [operation for operation in operations if operation.state == "EXECUTED"]
#
#
# def sort_operation(operations: list[Operation]) -> list[Operation]:
#     return sorted(operations, key=lambda x: x.date, reverse=True)
