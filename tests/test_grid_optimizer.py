import unittest
from aerospace_optimizer import grid_optimizer

class TestGridOptimizer(unittest.TestCase):

    def test_grid_optimizer_init(self):
        bounds = [(0, 10), (0, 10)]
        num_points = 5
        optimizer = grid_optimizer.GridOptimizer(bounds, num_points)
        self.assertEqual(optimizer.bounds, bounds)
        self.assertEqual(optimizer.num_points, num_points)

    def test_grid_optimizer_optimize(self):
        def objective_func(x):
            return x[0]**2 + x[1]**2

        bounds = [(0, 10), (0, 10)]
        num_points = 5
        optimizer = grid_optimizer.GridOptimizer(bounds, num_points)
        best_point, best_value = optimizer.optimize(objective_func)
        self.assertIsInstance(best_point, list)
        self.assertIsInstance(best_value, float)

    def test_grid_optimizer_test_grid_optimizer(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            grid_optimizer.test_grid_optimizer()
            mock_print.assert_called_once()

if __name__ == '__main__':
    unittest.main()
