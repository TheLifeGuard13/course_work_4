from pprint import pprint
from dotenv import load_dotenv
import os
import requests
from datetime import datetime

from classes.abstr_class import BaseAPI


class SuperJobAPI(BaseAPI):
    load_dotenv()

    def __init__(self):
        self.url = "https://api.superjob.ru/2.0/vacancies"
        self.secret_key = os.getenv("SUPER_JOB_KEY")

    def get_vacancies(self, text):
        vacancies = requests.get(self.url, headers={"X-Api-App-Id": self.secret_key},
                                 params={'keyword': {text}, "no_agreement": 1})
        return vacancies.json()


superjob_api = SuperJobAPI()
superjob_vacancies = superjob_api.get_vacancies("патентовед")

pprint(len(superjob_vacancies["objects"]))
pprint(superjob_vacancies["objects"][0])
new_list = []
for i in superjob_vacancies["objects"]:
    dict_ = {}
    dict_["ссылка"] = i["link"]
    dict_["опубликована"] = datetime.fromtimestamp(i["date_published"]).strftime("%d.%m.%Y")
    dict_["опыт"] = i["experience"]["title"]
    dict_["наименование"] = i["profession"]
    dict_["зарплата"] = {"от": i["payment_from"], "до": i["payment_to"]}
    dict_["график"] = i["type_of_work"]["title"]
    new_list.append(dict_)
pprint(new_list)
