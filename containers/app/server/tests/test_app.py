# tests/test_app.py
import unittest
import pytest
from agility_game.utils.app_utils import create_app


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main()
