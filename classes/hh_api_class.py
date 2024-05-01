import requests

from classes.abstr_class import BaseAPI


class HeadHunterAPI(BaseAPI):
    """
    Класс для выгрузки данных через API HeadHunter
    """

    def __init__(self) -> None:
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, text: str) -> list[dict]:
        """
        Получает вакансии через API HeadHunter
        """
        try:
            vacancies = requests.get(self.url, params={"text": {text}, "per_page": 100, "only_with_salary": True})
            return vacancies.json()["items"]
        except Exception as error:
            raise Exception(f"Ошибка {error}")
