from abc import ABC, abstractmethod


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass


class Saver(ABC):
    @abstractmethod
    def add_vacancies(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_vacancies(self, *args, **kwargs):
        pass
