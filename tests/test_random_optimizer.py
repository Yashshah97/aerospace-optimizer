import unittest
from aerospace_optimizer import random_optimizer

class TestRandomOptimizer(unittest.TestCase):

    def test_random_search(self):
        bounds = [(0.0, 10.0), (0.0, 10.0)]
        num_iterations = 1
        num_samples = 1

        def example_objective_function(parameters: tuple) -> float:
            x, y = parameters
            return (x - 2) ** 2 + (y - 3) ** 2

        best_objective, best_parameters = random_optimizer.random_search(
                example_objective_function, bounds, num_iterations, num_samples)

        self.assertIsInstance(best_objective, float)
        self.assertIsInstance(best_parameters, tuple)

    def test_optimization_strategy(self):
        self.assertEqual(len(random_optimizer.OptimizationStrategy), 3)

if __name__ == '__main__':
    unittest.main()
