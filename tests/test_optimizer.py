import unittest
from aerospace_optimizer import optimizer

class TestOptimizer(unittest.TestCase):

    def test_GridOptimizer(self):
        bounds = [(0, 10), (0, 10)]
        grid_optim = optimizer.GridOptimizer(bounds, 'grid')
        self.assertEqual(grid_optim.optimize(lambda x: sum(x)), [5, 5])

    def test_RandomOptimizer(self):
        bounds = [(0, 10), (0, 10)]
        random_optim = optimizer.RandomOptimizer(bounds, 'random', num_samples=100)
        self.assertEqual(len(random_optim.optimize(lambda x: sum(x))), 2)

    def test_AnnealingOptimizer(self):
        bounds = [(0, 10), (0, 10)]
        annealing_optim = optimizer.AnnealingOptimizer(bounds, 'annealing')
        self.assertEqual(annealing_optim.optimize(lambda x: sum(x)), [5, 5])

if __name__ == '__main__':
    unittest.main()
