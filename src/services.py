import re
import json
import logging

import pandas as pd


logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
console_handler.setFormatter(file_formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

DATAFRAME = pd.read_excel('../data/operations.xlsx')


def individual_transfer_search(df: pd.DataFrame) -> json:
    """Функция поиска транзакций по наличию Фамилии и заглавной букве имени в категории 'Переводы'"""
    pattern = r'[А-Я]\w+\s[А-Я]\.'
    filtered_info = df.loc[df['Категория'] == 'Переводы']
    logger.info("Отфильтровали транзакции по категории 'Переводы'")
    individual_transfer_list = []
    for index, row in filtered_info.iterrows():
        current_row = row.to_dict()
        if re.search(pattern, current_row['Описание']):
            individual_transfer_list.append(current_row)
            logger.info(f"Найдена транзакция с именем {current_row['Описание']} в описании")
    return json.dumps(individual_transfer_list, ensure_ascii=False)
