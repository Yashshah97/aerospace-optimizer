"""Smoke tests for grid_optimizer."""
import unittest

from aerospace_optimizer import grid_optimizer


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(grid_optimizer, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(grid_optimizer) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
