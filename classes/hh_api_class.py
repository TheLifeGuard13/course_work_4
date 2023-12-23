from classes.abstr_class import BaseAPI
import requests


class HeadHunterAPI(BaseAPI):
    """
    Класс для выгрузки данных через API HeadHunter
    """
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, text: str) -> list[dict]:
        """
        Получает вакансии через API HeadHunter
        """
        vacancies = requests.get(self.url, params={'text': {text}, "per_page": 100, "only_with_salary": True})
        return vacancies.json()["items"]
