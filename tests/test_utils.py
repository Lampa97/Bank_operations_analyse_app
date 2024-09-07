from datetime import datetime
from unittest.mock import Mock, patch

import pytest

from src.utils import fetch_currency_rate, fetch_s_p_500_stock, greeting, read_excel_file


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


def test_fetch_currency_rate():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 70.0}

    with patch("requests.get", return_value=mock_response):
        result = fetch_currency_rate(["USD"])
        assert result == [{"currency": "USD", "rate": 70.00}]


def test_fetch_currency_rate_false():
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.return_value = None

    with patch("requests.get", return_value=mock_response):
        assert fetch_currency_rate(["USS"]) == []


def test_fetch_s_p_500_stock():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": [{"open": 300.0}]}

    with patch("requests.get", return_value=mock_response):
        assert fetch_s_p_500_stock(["TSLA"]) == [{"stock": "TSLA", "price": 300.00}]


def test_fetch_s_p_500_stock_false():
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.return_value = None

    with patch("requests.get", return_value=mock_response):
        assert fetch_currency_rate(["EPPL"]) == []
