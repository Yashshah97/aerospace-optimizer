"""Smoke tests for test_optimizer."""
import unittest

from aerospace_optimizer import test_optimizer


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(test_optimizer, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(test_optimizer) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
