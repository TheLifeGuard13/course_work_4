from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        """
        Абстрактный метод получения вакансий через API
        """
        pass


class Saver(ABC):
    """
    Абстрактный класс для работы с файлом json
    """

    @abstractmethod
    def add_vacancies(self, *args, **kwargs):
        """
        Абстрактный метод сохранения вакансий в файл
        """
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, *args, **kwargs):
        """
        Абстрактный метод сохранения вакансий в файл
        """
        pass

    @abstractmethod
    def delete_vacancies(self, *args, **kwargs):
        """
        Абстрактный метод удаления файла вакансий
        """
        pass
