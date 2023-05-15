import pytest
from src import transactions as pay_


@pytest.fixture
def pay():
    return pay_.Transactions()


def test_set_date_correct(pay):
    pay.set_date('2022-05-15T10:50:58.294041')
    assert pay.get_date() == "15.05.2022"


def test_set_date_incorrect(pay):
    pay.set_date('202A-08-20T12:04:13.781725')
    assert pay.get_date() is None
    pay.set_date('2019-04-35T10:50:58.294041')
    assert pay.get_date() is None


def test_set_correct_operation_amount(pay):
    pay.set_operation_amount({'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}})
    assert pay.get_operation_amount() == ("21344.35", "руб.")


def test_set_incorrect_operation_amount_amount_1(pay):
    pay.set_operation_amount({'amount': '21344.3', 'currency': {'name': 'USD', 'code': 'USD'}})
    assert pay.get_operation_amount() == "Incorrect amount!"


def test_set_incorrect_operation_amount_amount_2(pay):
    pay.set_operation_amount({'amount': '-21344.35', 'currency': {'name': 'USD', 'code': 'USD'}})
    assert pay.get_operation_amount() == "Incorrect amount!"


def test_set_incorrect_operation_amount_amount_3(pay):
    pay.set_operation_amount({'amount': '', 'currency': {'name': 'USD', 'code': 'USD'}})
    assert pay.get_operation_amount() == "Incorrect amount or currency!"


def test_set_operation_amount_incorrect_amount_4(pay):
    pay.set_operation_amount({'amount': '', 'currency': {}})
    assert pay.get_operation_amount() == "Incorrect amount or currency!"


def test_set_description(pay):
    pay.set_description('Перевод с карты на карту')
    assert pay.get_description() == 'Перевод с карты на карту'


def test_set_operation_amount_incorrect_name(pay):
    pay.set_operation_amount({'amount': '21344.35', 'currency': {'name': '', 'code': 'USD'}})
    assert pay.get_operation_amount() == "Incorrect amount or currency!"


def test_set_description_none(pay):
    pay.set_description("")
    assert pay.get_description() is None


def test_set_description_not_str(pay):
    pay.set_description(True)
    assert pay.get_description() is None


def test_set_pay_from(pay):
    pay.set_pay_from('Счет 33355011456314142963')
    assert pay.get_pay_from() == ("Счет", "33355011456314142963")


def test_set_pay_from_empty(pay):
    pay.set_pay_from('')
    assert pay.get_pay_from() is None


def test_set_pay_from_incorrect(pay):
    pay.set_pay_from('Maestro 8609654751155')
    assert pay.get_pay_from() == "Incorrect account or card number!"


def test_set_pay_to(pay):
    pay.set_pay_to('Maestro 8602249654751155')
    assert pay.get_pay_to() == ("Maestro", "8602249654751155")


def test_set_pay_to_empty(pay):
    pay.set_pay_to('')
    assert pay.get_pay_to() is None


def test_set_pay_to_short_number(pay):
    pay.set_pay_to('Счет 4573591729755908868')
    assert pay.get_pay_to() == "Incorrect account or card number!"


def test_set_pay_to_incorrect_number(pay):
    pay.set_pay_to('МИР 521127741822846A9')
    assert pay.get_pay_to() == "Incorrect account or card number!"
