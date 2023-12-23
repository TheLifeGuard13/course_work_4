from dotenv import load_dotenv
import os
import requests

from classes.abstr_class import BaseAPI


class SuperJobAPI(BaseAPI):
    """
    Класс для выгрузки данных через API SuperJob
    """
    load_dotenv()

    def __init__(self):
        self.url = "https://api.superjob.ru/2.0/vacancies"
        self.secret_key = os.getenv("SUPER_JOB_KEY")

    def get_vacancies(self, text: str) -> list[dict]:
        """
        Получает вакансии через API SuperJob
        """
        vacancies = requests.get(self.url, headers={"X-Api-App-Id": self.secret_key},
                                 params={'keywords': {text}, "no_agreement": 1})
        return vacancies.json()["objects"]
