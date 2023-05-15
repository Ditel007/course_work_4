from datetime import datetime


class Transactions:

    def __init__(self):
        """
        - `id` — id транзакции
        - `date` — информация о дате совершения операции
        - `state` — статус перевода:
        - `EXECUTED`  — выполнена,
        - `CANCELED`  — отменена.
        - `operationAmount` — сумма операции и валюта
        - `description` — описание типа перевода
        - `from` — откуда (может отсутствовать)
        - `to` — куда
        """
        self.__id = None
        self.__state = None
        self.__date = None
        self.__operation_amount = None
        self.__description = None
        self.__from = None
        self.__to = None

    def __repr__(self):
        return f"Payment(" \
               f"id={self.__id}," \
               f"state=\"{self.__state}\"," \
               f"date=\"{self.__date}\"," \
               f"operation_amount={self.__operation_amount}," \
               f"description=\"{self.__description}\"," \
               f"from=\"{self.__from}\"," \
               f"to=\"{self.__to}\")"

    def set_id(self, id_operation):
        if type(id_operation) is int:
            self.__id = id_operation

    def set_state(self, state_operation):
        if state_operation.lower() == "executed":
            self.__state = state_operation.upper()

    def set_date(self, date):
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
            self.__date = date_obj.strftime('%d.%m.%Y')
        except ValueError:
            return "Invalid date format"

    def get_date(self):
        if self.__date == ValueError:
            return print("Invalid date format")
        else:
            return self.__date

    def set_operation_amount(self, operation_amount):
        amount = operation_amount.get('amount')
        currency = operation_amount.get('currency')
        currency_name = currency.get('name') if currency else None

        if amount and currency_name and type(currency_name) is str:
            if self.__check_operation_amount(amount):
                self.__operation_amount = (amount, currency_name)
            else:
                self.__operation_amount = "Incorrect amount!"

        else:
            self.__operation_amount = "Incorrect amount or currency!"

    @staticmethod
    def __check_operation_amount(amount):
        for_amount = str(amount).split(".")
        if len(for_amount) != 2:
            return False
        elif len(for_amount[1]) != 2:
            return False
        elif not for_amount[0].isdigit() or not for_amount[1].isdigit():
            return False
        elif int(for_amount[0]) < 0 or int(for_amount[1]) < 0:
            return False

        return True

    def get_operation_amount(self):
        return self.__operation_amount

    def set_description(self, description):
        if description and type(description) is str:
            self.__description = description

    def get_description(self):
        return self.__description

    def set_pay_from(self, pay_from):
        if pay_from:
            card_sep = pay_from.rsplit(" ", 1)
            card, number = card_sep
            if self.__check_pay_card(card, number):
                self.__from = (card, number)
            else:
                self.__from = "Incorrect account or card number!"

    @staticmethod
    def __check_pay_card(card, number):
        amount_digits = [16, 20]

        if not number.isdigit() or len(number) not in amount_digits:
            return False
        elif card.lower() == "счет" and len(number) != amount_digits[-1]:
            return False

        return True

    def get_pay_from(self):
        return self.__from

    def set_pay_to(self, pay_to):
        if pay_to:
            card_sep = pay_to.rsplit(" ", 1)
            card, number = card_sep
            if self.__check_pay_card(card, number):
                self.__to = (card, number)
            else:
                self.__to = "Incorrect account or card number!"

    def get_pay_to(self):
        return self.__to
