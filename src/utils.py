import datetime
from typing import List

import pandas as pd


def read_excel_file(path: str) -> List[dict]:
    info = pd.read_excel(path)
    return info.to_dict(orient="records")


def greeting(date: datetime.date) -> str:
    hour = int(date.strftime("%H"))
    if hour < 6:
        return "Доброй ночи"
    elif hour < 12:
        return "Доброе утро"
    elif hour < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"
