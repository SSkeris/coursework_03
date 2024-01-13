from src.func import is_ex_operations, sort_by_date, five_last, get_from, get_to, date_


def test_is_ex_operations():
    """Тест функции is_ex_operations"""
    test_list = [{"state": "EXEC", "date": "2019-07-03T18:35:29.512364"},
                 {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]
    assert is_ex_operations(test_list) == [
        {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]


def test_sort_by_date():
    """Тест функции sort_by_date"""
    test_list = [{"state": "EXEC", "date": "2019-07-03T18:35:29.512364"},
                 {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"}]
    assert sort_by_date(test_list) == [
        {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
        {"state": "EXEC", "date": "2019-07-03T18:35:29.512364"}]


def test_five_last():
    """Тест функции five_last"""
    test_list_2 = ['1', '1', '1', '1', '1', '1']
    assert len(five_last(test_list_2)) == 5


def test_get_from():
    """Тест функции get_from"""
    test_dict = {'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}
    test_dict_2 = {'to': 'Счет 35158586384610753655'}
    test_dict_3 = {'from': 'Maestro 2842878893689012', 'to': 'Счет 35158586384610753655'}
    assert get_from(test_dict) == 'Visa Classic 2842 87** **** 9012'
    assert get_from(test_dict_2) == "Новый клиент"
    assert get_from(test_dict_3) == 'Maestro 2842 87** **** 9012'


def test_get_to():
    """Тест функции get_to"""
    test_dict = {'from': 'Visa Classic 2842878893689012', 'to': 'Visa Classic 2842878893689012'}
    test_dict_2 = {'to': 'Счет 35158586384610753655'}
    assert get_to(test_dict) == 'Visa Classic **9012'
    assert get_to(test_dict_2) == "Счет **3655"


def test_date_():
    """Тест функции date_"""
    test_dict = {"date": "2019-08-26T10:50:58.294041"}
    assert date_(test_dict) == "26.08.2019"
