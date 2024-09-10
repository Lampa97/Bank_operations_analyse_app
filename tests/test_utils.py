from unittest.mock import Mock, patch

import pytest

from src.utils import fetch_currency_rate, fetch_s_p_500_stock, get_cards_info, get_top_5_transactions, greeting


@pytest.mark.parametrize(
    "date, result",
    [
        ("2022-03-08 5:45:0", "Доброй ночи"),
        ("2022-03-08 8:45:0", "Доброе утро"),
        ("2022-03-08 13:45:0", "Добрый день"),
        ("2022-03-08 19:45:0", "Добрый вечер"),
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


def test_get_cards_info(df_one_transaction):
    assert get_cards_info(df_one_transaction) == [{"last_digits": "5678", "total_spent": 3000.0, "cashback": 30.0}]


def test_get_top_5_transactions(df_5_transactions, top_5_transactions):
    assert get_top_5_transactions(df_5_transactions) == top_5_transactions
