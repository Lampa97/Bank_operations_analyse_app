from datetime import datetime
from unittest.mock import patch

import pytest

from src.utils import greeting, read_excel_file


def test_read_excel_file(df_one_transaction, one_transaction):
    with patch("pandas.read_excel", return_value=df_one_transaction):
        result = read_excel_file("path")
        assert result == one_transaction


@pytest.mark.parametrize(
    "date, result",
    [
        (datetime(2022, 3, 8, 5, 45, 0), "Доброй ночи"),
        (datetime(2022, 3, 8, 8, 45, 0), "Доброе утро"),
        (datetime(2022, 3, 8, 15, 45, 0), "Добрый день"),
        (datetime(2022, 3, 8, 18, 45, 0), "Добрый вечер"),
    ],
)
def test_greeting(date, result):
    assert greeting(date) == result
