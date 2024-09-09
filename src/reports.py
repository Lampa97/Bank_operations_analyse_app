import datetime
from typing import Optional

import pandas as pd

from src.logger import logger_setup

logger = logger_setup()


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Позволяет отфильтровать транзакции по описанию за последние 3 месяца с указанной даты"""
    if date:
        current_date = datetime.datetime.strptime(date, "%d.%m.%Y")
    else:
        current_date = datetime.datetime.today()
    logger.info(f"Получена дата: {current_date}")
    transactions["TimeStamp"] = pd.to_datetime(transactions["Дата платежа"], dayfirst=True)
    logger.info("Создали столбец 'TimeStamp'")
    transactions["Сегодня"] = current_date
    logger.info("Создали столбец 'Сегодня'")
    transactions["Прошло дней"] = (transactions["Сегодня"] - transactions["TimeStamp"]).dt.days
    logger.info("Создали столбец 'Прошло дней'")
    filtered_info = transactions.loc[
        (transactions["Категория"] == category)
        & (transactions["Прошло дней"] < 90)
        & (transactions["Прошло дней"] >= 0)
    ]
    logger.info(f"Отфильтровали транзакции по категории '{category}' за последние 3 месяца")
    del filtered_info["Сегодня"]
    logger.info("Удалили столбец 'Сегодня'")
    del filtered_info["Прошло дней"]
    logger.info("Удалили столбец 'Прошло дней'")
    del filtered_info["TimeStamp"]
    logger.info("Удалили столбец 'TimeStamp'")
    return filtered_info
