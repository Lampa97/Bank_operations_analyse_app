import pytest

from src.services import individual_transfer_search


def test_individual_transfer_search(individual_transactions, json_individual_transaction):
    assert individual_transfer_search(individual_transactions) == json_individual_transaction