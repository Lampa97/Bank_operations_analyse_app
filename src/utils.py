import datetime
import os
from typing import List

import pandas as pd
import requests
from dotenv import load_dotenv
import logging

load_dotenv()

CURRENCY_API_TOKEN = os.getenv("CURRENCY_API_KEY")
STOCK_API_TOKEN = os.getenv("STOCK_API_KEY")




def read_excel_file(path: str) -> pd.DataFrame:
    """Считывает информацию из excel файла"""
    return pd.read_excel(path)
    # return info.to_dict(orient="records")

def get_cards_info(df: pd.DataFrame) -> dict:
    filtered_info = df.loc[(df['Номер карты'].notnull()) & (df['Статус'] == 'OK') & (df['Сумма платежа'] < 0)]
    grouped_info = filtered_info.groupby('Номер карты')['Сумма операции'].sum()
    dict_info = grouped_info.to_dict()
    card_info = []
    for card_number, total_sum in dict_info.items():
        one_card_info = dict()
        one_card_info['last_digits'] = card_number[1:]
        one_card_info['total_spent'] = abs(total_sum)
        one_card_info['cashback'] = round(abs(total_sum) / 100, 2)
        card_info.append(one_card_info)
    return card_info


daf = read_excel_file('../data/operations.xlsx')

ss = get_cards_info(daf)

print(ss)

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


def fetch_currency_rate(currency_list: list) -> List[dict]:
    """Запрашивает и возвращает список курсов валют по отношению к рублю"""
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
    """Обращается к API и возвращает список цен акций заданных компаний"""
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
