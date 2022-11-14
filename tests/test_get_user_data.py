import pytest
from get_users_data.get_users_names import *

NUM_OF_PAGE1 = 1
NUM_OF_PAGE2 = 2
USER_DATA_ON_PAGE1 = 6
USER_DATA_ON_PAGE2 = 6
TOTAL_USER_DATA = 12


def test_get_data_from_page1():
    value = get_data(NUM_OF_PAGE1)
    assert isinstance(value, dict)


def test_get_data_from_page2():
    value = get_data(NUM_OF_PAGE2)
    assert isinstance(value, dict)


def test_user_data_from_page1():
    value = len(get_user_data(NUM_OF_PAGE1))
    assert value == USER_DATA_ON_PAGE1


def test_user_data_from_page2():
    value = len(get_user_data(NUM_OF_PAGE2))
    assert value == USER_DATA_ON_PAGE2


def test_user_data_from_all_pages():
    value = len(get_user_data_from_all_pages())
    assert value == TOTAL_USER_DATA
