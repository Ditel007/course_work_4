import json
from itertools import islice
import src.transactions as trns_


def load_json(path):
    with open(path, "r", encoding="utf-8") as json_file:
        payments = json.load(json_file)

    return payments


def get_recent_payments(path, count, parameters):
    lst = []
    payments = load_json(path)
    for i in payments:
        if len(i) > 1:
            lst.append(i)
    lst.sort(key=lambda x: x['date'])
    latest_payments_gen = latest_correct_payments(lst, parameters)
    successful_payments = islice(latest_payments_gen, count)

    return successful_payments


def latest_correct_payments(payments, parameters):
    for pay in payments[::-1]:
        if pay["state"].lower() == "executed":
            if parameters.issubset(set(pay.keys())):
                yield pay


def create_payment(pay_information: dict):
    payment = trns_.Transactions()
    payment.set_id(pay_information.get("id"))
    payment.set_state(pay_information.get("state"))
    payment.set_date(pay_information.get("date"))
    payment.set_operation_amount(pay_information.get("operationAmount"))
    payment.set_description(pay_information.get("description"))
    payment.set_pay_from(pay_information.get("from"))
    payment.set_pay_to(pay_information.get("to"))

    return payment


def show_payment(pay):
    date = pay.get_date()
    description = pay.get_description()
    pay_from = pay.get_pay_from()
    pay_to = pay.get_pay_to()
    operation_amount = pay.get_operation_amount()

    print()
    print(f'{date} {description}')
    if pay_from:
        print(f"{pay_from[0]} \033[34m{hide(pay_from[1])}\033[0m ", end=" ")
    print(f"-\033[33m> \033[0m{pay_to[0]} \033[34m{hide(pay_to[1])}")
    print(f"\033[32m{operation_amount[0]}\033[0m {operation_amount[1]}")


def hide(number):
    if len(number) == 16:
        number_hide = number[:6] + "*" * 6 + number[12:]
        return " ".join([number_hide[i:i + 4] for i in range(0, len(number_hide), 4)])

    elif len(number) == 20:
        return number.replace(number[:-4], "**")
