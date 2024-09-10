from src.reports import spending_by_category, file_writer
import pandas

@file_writer()
def test_spending_by_category(df_5_transactions_for_report, df_filtered_by_category):
    assert spending_by_category(df_5_transactions_for_report, 'Переводы') == pandas.DataFrame()
