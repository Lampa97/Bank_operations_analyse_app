from idlelib.pyparse import trans
from typing import Optional
import pandas as pd
import logging
import datetime
import re

def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    if date:
        current_date = datetime.datetime.strptime(date, "%d.%m.%Y")
    else:
        current_date = datetime.datetime.today()
    transactions['TimeStamp'] = pd.to_datetime(transactions['Дата платежа'], dayfirst=True)
    transactions['Сегодня'] = current_date
    transactions['Прошло дней'] = (transactions['Сегодня'] - transactions['TimeStamp']).dt.days
    filtered_info = transactions.loc[(transactions['Категория'] == category) & (transactions['Прошло дней'] < 90) & (transactions['Прошло дней'] >= 0)]
    del filtered_info['Сегодня']
    del filtered_info['Прошло дней']
    del filtered_info['TimeStamp']
    return filtered_info
