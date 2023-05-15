import pytest as pytest
import json

from src.utils import load_json, get_recent_payments, hide, create_payment


def test_load_file_positive():
    filename = "/Users/macditel/PycharmProjects/course_work_4/tests/src/test_load.json"
    assert load_json(filename) == [{'x': 312, 'z': 123}, {'c': 1234, 'v': 1213}]


def test_load_non_exist_file():
    filename = "/Users/macditel/PycharmProjects/course_work_4/tests/src/testy_incorrect_load.json"
    with pytest.raises(FileNotFoundError):
        assert load_json(filename)


def test_load_file_negative():
    filename = "/Users/macditel/PycharmProjects/course_work_4/tests/src/test_incorrect_load.json"
    try:
        load_json(filename)
    except json.JSONDecodeError as e:
        assert "Expecting property name" in str(e)
    else:
        raise AssertionError("Expected JSONDecodeError was not raised")


def test_recent_payments():
    filename = "/Users/macditel/PycharmProjects/course_work_4/tests/src/test_recent_payments.json"
    parameters = {"id", "date", "state", "operationAmount", "description", "to"}
    assert get_recent_payments(filename, 4, parameters)


def test_hide():
    # Test valid input
    assert hide("1234567890123456") == "1234 56** **** 3456"
    assert hide("75106830613657916952") == "**6952"


