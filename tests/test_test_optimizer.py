import unittest
import sys
from aerospace_optimizer import test_optimizer

class TestTestOptimizer(unittest.TestCase):
    def test_test_grid_search(self) -> None:
        """Test test grid search function."""
        self.assertIsInstance(test_optimizer.TestOptimizer.test_grid_search, unittest.TestCase)

    def test_test_random_search(self) -> None:
        """Test test random search function."""
        self.assertIsInstance(test_optimizer.TestOptimizer.test_random_search, unittest.TestCase)

    def test_test_annealing_search(self) -> None:
        """Test test annealing search function."""
        self.assertIsInstance(test_optimizer.TestOptimizer.test_annealing_search, unittest.TestCase)

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
