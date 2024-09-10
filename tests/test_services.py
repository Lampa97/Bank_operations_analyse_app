import pytest

from src.services import individual_transfer_search

def test_individual_transfer_search(individual_transactions, list_individual_transaction):
    assert individual_transfer_search(individual_transactions) == list_individual_transaction

def test_individual_transfer_search_empty(df_5_transactions):
    assert individual_transfer_search(df_5_transactions) == []