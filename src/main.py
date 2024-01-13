from func import load_operations, sort_by_date, is_ex_operations, five_last, get_from, get_to, date_

operations = load_operations()  # загружает список операций
ex_operations = is_ex_operations(operations)  # сортирует операции по ключу "EXECUTED"
sorted_operations = sort_by_date(ex_operations)  # сортирует операции по дате
last_operations = five_last(sorted_operations)  # 5 последних операций

for i in last_operations:  # вывод данных по операциям
    print(f"{date_(i)} {i['description']}")
    print(f"{get_from(i)} -> {get_to(i)}")
    print(f"{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n")
