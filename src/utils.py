import datetime
import os
from typing import List

import requests
from dotenv import load_dotenv

load_dotenv()

CURRENCY_API_TOKEN = os.getenv("CURRENCY_API_KEY")
STOCK_API_TOKEN = os.getenv("STOCK_API_KEY")

import pandas as pd


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


def fetch_currency_rate(currency: str) -> float | bool:
    """Запрашивает и возвращает курс валюты по отношению к рублю"""
    url = f"https://api.apilayer.com/fixer/convert?to=RUB&from={currency}&amount=1"

    headers = {"apikey": CURRENCY_API_TOKEN}

    response = requests.get(url, headers=headers)

    status_code = response.status_code
    if status_code == 200:
        result = response.json()
        return float(result["result"])
    else:
        return False


def fetch_s_p_500_stock(stock: str) -> float | bool:
    """Обращается к API и возвращает цену акции компании"""
    url = f"https://api.marketstack.com/v1/intraday?access_key={STOCK_API_TOKEN}"

    querystring = {"symbols": stock}

    response = requests.get(url, params=querystring)
    status_code = response.status_code
    if status_code == 200:
        result = response.json()
        return float(result["data"][0]["open"])
    else:
        return False
