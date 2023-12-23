import json
import os
from pathlib import Path

from classes.abstr_class import Saver


FILE_PATH = Path(__file__).parent.parent.joinpath("data", "example.json")


class JSONSaver(Saver):
    """
    Класс для работы с файлом json
    """
    def add_vacancies(self, vacancies: list[dict]) -> None:
        """
        Сохраняет переданные вакансии в файл json
        """
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def get_vacancies_by_salary(self, salary_from: int, salary_to: int) -> list[dict]:
        """
        Фильтрует вакансии в файл json по зарплате (по нижнему и верхнему порогу)
        """
        with open(FILE_PATH) as file:
            data = json.load(file)
        return [vacancy for vacancy in data if vacancy["Зарплата от"] >= salary_from
                and vacancy["Зарплата до"] <= salary_to]

    def delete_vacancies(self) -> None:
        """
        Удаляет файл с вакансиями
        """
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
