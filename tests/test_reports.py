from unittest.mock import MagicMock, patch

import pandas as pd

from src.reports import spending_by_category


def test_spending_by_category(df_5_transactions_for_report, df_filtered_by_category):

    with patch("pandas.DataFrame.to_csv", MagicMock()) as mock_to_csv:

        result_df = spending_by_category(df_5_transactions_for_report, "Переводы", date="10.01.2018")

        mock_to_csv.assert_called_once_with("data/filtered_operations.csv", encoding="utf-8")

        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), df_filtered_by_category.reset_index(drop=True))
