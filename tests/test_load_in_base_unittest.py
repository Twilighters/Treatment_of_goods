import unittest
from tests.constant_test_cases import PUBLIC_TEST_CASES, SECRET_TEST_CASES
from main import (
    load_in_base,
    engine,
)  # Импорт функции load_in_base из домашнего задания
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class LoadInBaseTestCase(unittest.TestCase):
    """Такие же тестовые случаи, но реализованные через unittest."""

    def setUp(self):
        """Начальные условия для тестов."""
        self.all_test_cases = PUBLIC_TEST_CASES + SECRET_TEST_CASES

    def test_load_in_base(self):
        """Тесирование функции подсчета кратеров."""
        for test_case in self.all_test_cases:
            test_input = test_case.get("test_input")
            expected = test_case.get("expected")

            self.assertEqual(load_in_base(test_input, engine), expected)
