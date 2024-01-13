import json
from datetime import datetime


def load_operations() -> list:
    """Возвращает список из файла 'operations.json'"""
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


def is_ex_operations(i: list) -> list:
    """Сортирует список по ключу 'EXECUTED'"""
    ex_list = []
    for n in i:
        if n.get("state") == "EXECUTED":
            ex_list.append(n)
    return ex_list


def sort_by_date(i: list) -> list:
    """Сортирует список по ключу 'date' по убыванию"""
    sorted_date = []
    for n in i:
        if n.get("date"):
            sorted_date.append(n)
    sorted_date.sort(key=lambda x: x.get('date'), reverse=True)
    return sorted_date


def five_last(i: list) -> list:
    """Выбирает 5 операций из списка сортированных по дате операций"""
    count = 0
    last_list = []
    for n in i:
        last_list.append(n)
        count += 1
        if count == 5:
            break
    return last_list


def get_from(i: dict) -> str:
    """Получение данных отправителя перевода, содержит тип счета и приватный номер счета"""
    if i.get('from') == None:
        return "Новый клиент"
    else:
        bill = i['from']
        if len(bill.split()) == 2:
            bill_number = bill.split()[-1]
            bill_type = (bill.split()[0])
            return f"{bill_type} {bill_number[:4]} {bill_number[4:6]}** **** {bill_number[-4:]}"
        else:
            bill_number = bill.split()[-1]
            bill_type = (bill.split()[0]) + " " + (bill.split()[1])
            return f"{bill_type} {bill_number[:4]} {bill_number[4:6]}** **** {bill_number[-4:]}"


def get_to(i: dict) -> str:
    """Получение данных получателя перевода, содержит тип счета и приватный номер счета"""
    bill_to = i.get('to')
    if len(bill_to.split()) == 2:
        bill_number_to = bill_to.split()[-1]
        bill_type_to = (bill_to.split()[0])
        return f"{bill_type_to} **{bill_number_to[-4:]}"
    else:
        bill_number_to = bill_to.split()[-1]
        bill_type_to = (bill_to.split()[0]) + " " + (bill_to.split()[1])
        return f"{bill_type_to} **{bill_number_to[-4:]}"


def date_(i: dict) -> str:
    date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return date
