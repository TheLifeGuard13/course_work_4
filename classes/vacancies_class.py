class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(
        self,
        vacancy_id: int,
        vacancy_url: str,
        vacancy_pub_date: str,
        experience: str,
        vacancy_name: str,
        salary_currency: str,
        salary_from: int | None,
        salary_limit: int | None,
        work_schedule: str,
        salary_status: bool = False,
    ):
        self.vacancy_id = int(vacancy_id)
        self.vacancy_url = vacancy_url
        self.vacancy_pub_date = vacancy_pub_date
        self.experience = experience
        self.vacancy_name = vacancy_name
        self.salary_currency = salary_currency
        self.salary_status = salary_status
        self.salary_from = int(self.convert_net_to_gross(salary_from))
        self.salary_limit = int(self.convert_net_to_gross(salary_limit))
        self.work_schedule = work_schedule

    def convert_net_to_gross(self, salary: int | None) -> int:
        """
        Конвертирует зарплату net в зарплату gross
        """
        try:
            if salary is None:
                return 0
            elif self.salary_status:
                return int(salary * 1.13)
            return salary
        except Exception as error:
            raise Exception(f"Ошибка {error}")

    def __str__(self) -> str:
        return f"{self.vacancy_name},{self.salary_currency}, {self.salary_from}"
