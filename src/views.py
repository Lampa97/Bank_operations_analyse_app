import datetime
import json

import pandas as pd

from src.utils import fetch_currency_rate, fetch_s_p_500_stock, get_cards_info, get_top_5_transactions, greeting

with open("user_settings.json", "r", encoding="utf-8") as file:
    user_data = json.load(file)

USER_STOCKS = user_data["user_stocks"]
USER_CURRENCIES = user_data["user_currencies"]
DATAFRAME = pd.read_excel("data/operations.xlsx")
DATE_NOW_STRING = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def greetings_info(date: str) -> dict:
    """Записывает информацию о пользователе для отображения на главной странице"""
    user_greeting = dict()
    user_greeting["greeting"] = greeting(date)
    user_greeting["cards"] = get_cards_info(DATAFRAME)
    user_greeting["top_transactions"] = get_top_5_transactions(DATAFRAME)
    user_greeting["currency_rates"] = fetch_currency_rate(USER_CURRENCIES)
    user_greeting["stock_prices"] = fetch_s_p_500_stock(USER_STOCKS)
    return user_greeting


