import pytest
from src import funcs


@pytest.fixture
def dict_fixture():
    return {
            "id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации", "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
            }


@pytest.fixture
def dict_fixture_miss():
    return {
            "id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
           }


@pytest.fixture
def new_fixture():
    return [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"},
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"}]


def test_get_date(dict_fixture):
    assert funcs.get_date(dict_fixture["date"]) == "26.08.2019"


def test_get_description(dict_fixture, dict_fixture_miss):
    assert funcs.get_description(dict_fixture.get("description", None)) == "Перевод организации"
    assert funcs.get_description(dict_fixture_miss.get("description", None)) == "No description"


def test_get_sender(dict_fixture, dict_fixture_miss):
    assert funcs.get_sender(dict_fixture["from"]) == "Maestro 1596 83** **** 5199"
    assert funcs.get_sender(dict_fixture_miss.get("from", None)) == "No info about sender"


def test_get_recipient(dict_fixture, dict_fixture_miss):
    assert funcs.get_recipient(dict_fixture["to"]) == "Счет **9589"
    assert funcs.get_recipient(dict_fixture_miss.get("to", None)) == "No info about recipient"


def test_get_all_data(dict_fixture):
    assert funcs.get_all_data(dict_fixture) == ("26.08.2019", "Перевод организации",
                                                "Maestro 1596 83** **** 5199", "Счет **9589",
                                                "31957.58 руб.")


def test_get_presentation():
    data = ("date", "desc", "sender", "recip", "amount")
    assert funcs.get_presentation(data) == 'date desc\nsender -> recip\namount\n'


def test_sorted_data(new_fixture):
    assert funcs.get_sorted_data(new_fixture) == [{'id': 441945886, 'state': 'EXECUTED',
                                                   'date': '2019-08-26T10:50:58.294041'},
                                                   {'id': 41428829, 'state': 'EXECUTED',
                                                    'date': '2019-07-03T18:35:29.512364'}]
