import pytest
from averages_comparator import AveragesComparator


@pytest.fixture
def list1():
    return [1, 2, 3, 4, 5, 6, 7]  # 4


@pytest.fixture
def list2():
    return [3, 4, 5, 6, 7]  # 5


def test_init(list1, list2):
    """Проверка верной инициализации класса"""
    lists = AveragesComparator(list1, list2)
    assert lists.list1 == list1
    assert lists.list2 == list2


def test_get_average_lists(list1, list2):
    """Проверка вычисления средних значений списков"""
    lists = AveragesComparator(list1, list2)
    assert lists.get_average_lists() == (4, 5)


def test_first_average_large(list1, list2):
    """Проверка случая, когда среднее значение первого списка больше второго"""
    lists = AveragesComparator(list2, list1)
    assert lists.compare_lists() == "Первый список имеет большее среднее значение"


def test_second_average_large(list1, list2):
    """Проверка случая, когда среднее значение второго списка больше первого"""
    lists = AveragesComparator(list1, list2)
    assert lists.compare_lists() == "Второй список имеет большее среднее значение"


def test_both_average_equal(list1):
    """Проверка случая, когда средние значения списков равны"""
    lists = AveragesComparator(list1, list1)
    assert lists.compare_lists() == "Средние значения равны"


def test_first_list_empty(list1):
    """Проверка случая, когда первый список пуст"""
    lists = AveragesComparator([], list1)
    assert lists.compare_lists() == "Второй список имеет большее среднее значение"


def test_second_list_empty(list1):
    """Проверка случая, когда второй список пуст"""
    lists = AveragesComparator(list1, [])
    assert lists.compare_lists() == "Первый список имеет большее среднее значение"


def test_both_lists_empty():
    """Проверка случая, когда оба списка пусты"""
    lists = AveragesComparator([], [])
    assert lists.compare_lists() == "Средние значения равны"
