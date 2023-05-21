import pytest
from src import load_data


def test_data_load():
    assert load_data.load_data("file_for_test.txt") == '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]'
