"""
Unit tests for optimizer classes.

This module contains unit tests for the various optimizer strategies used in the
aerospace parameter optimizer.
"""

import unittest
from typing import List, Dict

class TestOptimizer(unittest.TestCase):
    def test_grid_search(self) -> None:
        """Test grid search strategy."""
        from aerospace_optimizer.strategies.grid_search import GridSearch
        grid = GridSearch(10)
        self.assertEqual(grid.num_points, 100)

    def test_random_search(self) -> None:
        """Test random search strategy."""
        from aerospace_optimizer.strategies.random_search import RandomSearch
        random = RandomSearch(10)
        self.assertEqual(random.num_points, 10)

    def test_annealing_search(self) -> None:
        """Test annealing search strategy."""
        from aerospace_optimizer.strategies.annealing_search import AnnealingSearch
        anneal = AnnealingSearch(10)
        self.assertEqual(anneal.temperature, 1.0)

class TestOptimizerStrategy(unittest.TestCase):
    def test_grid_search_strategy(self) -> None:
        """Test grid search strategy."""
        from aerospace_optimizer.strategies.grid_search import GridSearchStrategy
        grid = GridSearchStrategy()
        self.assertIsInstance(grid.search(), List[Dict[str, float]])

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
