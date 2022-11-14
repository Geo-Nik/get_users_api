import pytest
from get_users_data.get_users_names import *


# Sets of ranges for the testcases
SET1 = (1, 3)
SET2 = (5, 8)
SET3 = (5, 5)
SET4 = ("a", 8)
SET5 = (5, "a")
SET6 = ("a", "b")
SET7 = (3, 1)
SET8 = (-2, 1)
SET9 = (1, -1)
SET10 = (-3, -5)


def test_get_user_full_name_list_set1():
    value = get_user_full_name_list(SET1[0], SET1[1])
    assert value == ["Emma Wong", "George Bluth", "Janet Weaver"]


def test_get_user_full_name_list_set2():
    value = get_user_full_name_list(SET2[0], SET2[1])
    assert value == [
        "Charles Morris",
        "Lindsay Ferguson",
        "Michael Lawson",
        "Tracey Ramos",
    ]


def test_get_user_full_name_list_set3():
    value = get_user_full_name_list(SET3[0], SET3[1])
    assert value == ["Charles Morris"]


def test_get_user_full_name_list_set4():
    value = get_user_full_name_list(SET4[0], SET4[1])
    assert value == []


def test_get_user_full_name_list_set5():
    value = get_user_full_name_list(SET5[0], SET5[1])
    assert value == []


def test_get_user_full_name_list_set6():
    value = get_user_full_name_list(SET6[0], SET6[1])
    assert value == []


def test_get_user_full_name_list_set7():
    value = get_user_full_name_list(SET7[0], SET7[1])
    assert value == []


def test_get_user_full_name_list_set8():
    value = get_user_full_name_list(SET8[0], SET8[1])
    assert value == []


def test_get_user_full_name_list_set9():
    value = get_user_full_name_list(SET9[0], SET9[1])
    assert value == []


def test_get_user_full_name_list_set10():
    value = get_user_full_name_list(SET10[0], SET10[1])
    assert value == []
