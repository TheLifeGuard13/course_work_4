import json
import os
from pathlib import Path

from classes.abstr_class import Saver


# FILE_PATH = Path(__file__).parent.parent.joinpath("data", "example.json")


class JSONSaver(Saver):
    def add_vacancies(self, vacancies):
        with open("example.json", "w") as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary_from, salary_to):
        with open("example.json") as file:
            data = json.load(file)
        return [vacancy for vacancy in data if vacancy["Зарплата от"] >= salary_from
                and vacancy["Зарплата до"] <= salary_to]

    def delete_vacancies(self):
        if os.path.exists("example.json"):
            os.remove("example.json")
