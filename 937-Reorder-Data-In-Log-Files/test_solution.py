from solution import *

test_digits = "a1 9 2 3 1"
test_letters = "a2 act coke zero"


def test_get_log_type():
    assert getLogType(test_digits) == Logs.DIGITS
    assert getLogType(test_letters) == Logs.LETTERS


def test_get_log_id():
    assert getLogId(test_digits) == "a1"
    assert getLogId(test_letters) == "a2"


def test_get_log_content():
    assert getLogContent(test_digits) == "9 2 3 1"
    assert getLogContent(test_letters) == "act coke zero"
