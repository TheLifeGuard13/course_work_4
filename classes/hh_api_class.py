from classes.abstr_class import BaseAPI
import requests
from pprint import pprint
from datetime import datetime


class HeadHunterAPI(BaseAPI):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, text):
        vacancies = requests.get(self.url, params={'text': {text}, "per_page": 100, "only_with_salary": True})
        return vacancies.json()

    def net_to_gross(self):
        pass


hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("патентовед")

pprint(len(hh_vacancies["items"]))
# pprint(hh_vacancies["items"][0])
new_list = []
for i in hh_vacancies["items"]:
    dict_ = {}
    dict_["ссылка"] = i["alternate_url"]
    dict_["опубликована"] = datetime.fromisoformat(i["published_at"]).strftime("%d.%m.%Y")
    dict_["опыт"] = i["experience"]["name"]
    dict_["наименование"] = i["name"]
    dict_["зарплата"] = i["salary"]["from"]
    dict_["зарплата_гросс"] = i["salary"]["gross"]
    dict_["график"] = i["schedule"]["name"]
    new_list.append(dict_)
pprint(new_list)
