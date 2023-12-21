class Vacancy:
    def __init__(self, vacancy_id: int,
                 vacancy_url: str,
                 vacancy_pub_date: str,
                 experience: str,
                 vacancy_name: str,
                 salary_currency: str,
                 salary_from: int | None,
                 salary_limit: int | None,
                 work_schedule: str,
                 salary_status: bool = False):
        self.vacancy_id = int(vacancy_id)
        self.vacancy_url = vacancy_url
        self.vacancy_pub_date = vacancy_pub_date
        self.experience = experience
        self.vacancy_name = vacancy_name
        self.salary_currency = salary_currency
        self.salary_status = salary_status
        self.salary_from = self.convert_net_to_gross(salary_from)
        self.salary_limit = self.convert_net_to_gross(salary_limit)
        self.work_schedule = work_schedule

    def convert_net_to_gross(self, salary):
        if salary is None:
            return 0
        elif self.salary_status:
            return round(salary * 1.13, 2)
        return salary

    def __str__(self):
        return f"""{self.vacancy_id}, {self.vacancy_url}, {self.vacancy_pub_date}, {self.experience}, {self.vacancy_name},{self.salary_currency}, {self.salary_from}, {self.salary_limit}, {self.work_schedule}, {self.salary_status}"""



# Создать класс для работы с вакансиями.
# В этом классе самостоятельно определить атрибуты, такие как название вакансии,
# ссылка на вакансию, зарплата, краткое описание или требования и т. п. (не менее четырех).
# Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные,
# которыми инициализируются его атрибуты.
