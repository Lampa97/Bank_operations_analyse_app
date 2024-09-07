import datetime
import os
from typing import List

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

CURRENCY_API_TOKEN = os.getenv("CURRENCY_API_KEY")
STOCK_API_TOKEN = os.getenv("STOCK_API_KEY")




def read_excel_file(path: str) -> List[dict]:
    """Считывает информацию из excel файла"""
    info = pd.read_excel(path)
    return info.to_dict(orient="records")


def greeting(date: datetime.date) -> str:
    """Возвращает строку с приветствием в зависимости от времени суток"""
    hour = int(date.strftime("%H"))
    if hour < 6:
        return "Доброй ночи"
    elif hour < 12:
        return "Доброе утро"
    elif hour < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"

def cards_info(transactions_info: List[dict]) -> List[dict]:
    pass


def fetch_currency_rate(currency_list: list) -> List[dict]:
    """Запрашивает и возвращает курс валюты по отношению к рублю"""
    currency_rates_info = []
    for currency in currency_list:
        url = f"https://api.apilayer.com/fixer/convert?to=RUB&from={currency}&amount=1"

        headers = {"apikey": CURRENCY_API_TOKEN}

        response = requests.get(url, headers=headers)
        status_code = response.status_code
        if status_code == 200:
            current_currency = {"currency": currency}
            result = response.json()
            rate = round(float(result["result"]), 2)
            current_currency["rate"] = rate
            currency_rates_info.append(current_currency)
        else:
            continue
    return currency_rates_info


def fetch_s_p_500_stock(stock_list: list) -> List[dict]:
    """Обращается к API и возвращает цену акции компании"""
    stock_prices_info = []
    for stock in stock_list:
        url = f"https://api.marketstack.com/v1/intraday?access_key={STOCK_API_TOKEN}"

        querystring = {"symbols": stock}

        response = requests.get(url, params=querystring)
        status_code = response.status_code
        if status_code == 200:
            current_stock = {"stock": stock}
            result = response.json()
            stock_price = round(float(result["data"][0]["open"]), 2)
            current_stock["price"] = stock_price
            stock_prices_info.append(current_stock)
        else:
            continue
    return stock_prices_info
