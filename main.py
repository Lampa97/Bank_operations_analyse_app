import re

from src.reports import spending_by_category
from src.services import individual_transfer_search
from src.views import DATAFRAME, DATE_NOW_STRING, greetings_info


def main() -> None:
    user_choice = input(
        """Пожалуйста, выберите действие:
    1. Записать информацию о пользователе для главной страницы
    2. Использовать сервис поиска транзакций по категории 'Переводы' и наличию фамилии и инициала
    3. Создать отчет о транзакциях за последние 3 месяца по заданному описанию\n"""
    )
    if user_choice == "1":
        input_date = input(
            "Введите дату в формате YYYY-MM-DD hh:mm:ss или оставьте поле пустым для использования сегодняшней даты\n"
        )
        if re.match(r"\d{4}[-./]\d{2}[-./]\d{2}\s\d{2}:\d{2}:\d{2}", input_date):
            date = input_date
        else:
            date = DATE_NOW_STRING
        greetings_info(date)
    elif user_choice == "2":
        individual_transfer_search(DATAFRAME)
    elif user_choice == "3":
        user_category = input("Введите категорию по которой вы хотите отфильтровать транзакции: \n")
        input_date = input(
            "Введите дату в формате dd.mm.yyyy или оставьте поле пустым для использования сегодняшней даты \n"
        )
        if re.match(r"\d{2}.\d{2}.\d{4}", input_date):
            date = input_date
        else:
            date = None
        spending_by_category(DATAFRAME, user_category, date)
    else:
        print("К сожалению такой опции нет. Работа программы остановлена.")
    return None


if __name__ == "__main__":
    main()
