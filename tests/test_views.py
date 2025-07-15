from unittest.mock import patch

from src.views import greetings_info


def test_greetings_info():

    mock_greeting = "Доброе утро"
    mock_cards_info = [
        {"last_digits": "5814", "total_spent": 1262.00, "cashback": 12.62},
        {"last_digits": "7512", "total_spent": 7.94, "cashback": 0.08},
    ]
    mock_top_transactions = [
        {
            "date": "21.12.2021",
            "amount": 1198.23,
            "category": "Переводы",
            "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        },
        {"date": "20.12.2021", "amount": 829.00, "category": "Супермаркеты", "description": "Лента"},
        {"date": "20.12.2021", "amount": 421.00, "category": "Различные товары", "description": "Ozon.ru"},
        {"date": "16.12.2021", "amount": -14216.42, "category": "ЖКХ", "description": "ЖКУ Квартира"},
        {"date": "16.12.2021", "amount": 453.00, "category": "Бонусы", "description": "Кешбэк за обычные покупки"},
    ]
    mock_currency_rates = [{"USD": 74.5}, {"EUR": 89.1}]
    mock_stock_prices = [{"AAPL": 150.3}, {"MSFT": 305.7}]

    with patch("src.views.greeting", return_value=mock_greeting) as mock_greet, patch(
        "src.views.get_cards_info", return_value=mock_cards_info
    ) as mock_cards, patch(
        "src.views.get_top_5_transactions", return_value=mock_top_transactions
    ) as mock_top_transactions, patch(
        "src.views.fetch_currency_rate", return_value=mock_currency_rates
    ) as mock_currency, patch(
        "src.views.fetch_s_p_500_stock", return_value=mock_stock_prices
    ) as mock_stocks:

        mock_greet.side_effect = lambda date: mock_greeting
        mock_cards.side_effect = lambda df: mock_cards_info
        mock_top_transactions.side_effect = lambda df: mock_top_transactions
        mock_currency.side_effect = lambda currencies: mock_currency_rates
        mock_stocks.side_effect = lambda stocks: mock_stock_prices

        result = greetings_info("2024-09-10 14:15:30")

        mock_greet.assert_called_once_with("2024-09-10 14:15:30")
        mock_cards.assert_called_once()
        mock_top_transactions.assert_called_once()
        mock_currency.assert_called_once()
        mock_stocks.assert_called_once()

        expected_result = {
            "greeting": mock_greeting,
            "cards": mock_cards_info,
            "top_transactions": mock_top_transactions,
            "currency_rates": mock_currency_rates,
            "stock_prices": mock_stock_prices,
        }

        assert result == expected_result
