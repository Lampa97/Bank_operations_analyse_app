import json
import re

import pandas as pd

from src.logger import logger_setup

logger = logger_setup()


def individual_transfer_search(df: pd.DataFrame) -> None:
    """Функция поиска транзакций по наличию Фамилии и заглавной букве имени в категории 'Переводы'"""
    pattern = r"[А-Я]\w+\s[А-Я]\."
    filtered_info = df.loc[df["Категория"] == "Переводы"]
    logger.info("Отфильтровали транзакции по категории 'Переводы'")
    individual_transfer_list = []
    for index, row in filtered_info.iterrows():
        current_row = row.to_dict()
        if re.search(pattern, current_row["Описание"]):  # ищем имя в соответствии с паттерном
            individual_transfer_list.append(current_row)
            logger.info(f"Найдена транзакция с именем {current_row['Описание']} в описании")
    with open("data/individual_transfer.json", "w", encoding="utf-8") as json_file:
        json.dump(individual_transfer_list, json_file, ensure_ascii=False, indent=4)
