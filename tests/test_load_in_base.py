import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import (
    load_in_base,
    engine,
)  # Импорт функции load_in_base из домашнего задания
from tests.constant_test_cases import PUBLIC_TEST_CASES, SECRET_TEST_CASES

ALL_TEST_CASES = PUBLIC_TEST_CASES + SECRET_TEST_CASES


def test_load_in_base():
    for test_case in ALL_TEST_CASES:
        test_input = test_case.get("test_input")
        expected = test_case.get("expected")
        assert load_in_base(test_input, engine) == expected
