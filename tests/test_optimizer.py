"""Smoke tests for optimizer."""
import unittest

from aerospace_optimizer import optimizer


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(optimizer, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(optimizer) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
