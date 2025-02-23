from src.API import HeadHunterAPI
# from src.db import DBCreate
# from src.DBManager import DBManager
from src.employers import Employers
from src.vacancies import Vacancies


def main():
    print("=" * 100)
    print("Начало работы")

    default_companies_list = [
        "Альфа-Банк",
        "Т-Банк",
        "Самокат (ООО Умный ритейл)",
        "СОГАЗ",
        "ПАО Ростелеком",
        "Rusprofile",
        "Контур",
        "Нетология",
        "РМК",
        "УГМК",
    ]
    data = HeadHunterAPI().get_data(default_companies_list)

    # create_data_base = DBCreate()
    # create_data_base.create_database()

    employers_list = Employers().get_employers(data)
    # for i in employers_list:
    #     print(i)

    vacancies_list = []
    id_data = Vacancies().get_id(data)
    for i in id_data:
        vacancies_list += Vacancies().get_vacancies(i)
        # print(vacancies_list)

if __name__ == "__main__":
    main()