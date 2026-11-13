import unittest
from aerospace_optimizer import simulated_annealing

class TestSimulatedAnnealing(unittest.TestCase):

    def test_simulated_annealing_init(self):
        sa = simulated_annealing.SimulatedAnnealing(100, 0.1)
        self.assertEqual(sa.initial_temperature, 100)
        self.assertEqual(sa.cooling_rate, 0.1)

    def test_simulated_annealing_initialize(self):
        sa = simulated_annealing.SimulatedAnnealing(100, 0.1)
        solution = [1, 2, 3]
        sa.initialize(solution)
        self.assertEqual(sa.current_solution, solution)
        self.assertEqual(sa.best_solution, solution)

    def test_simulated_annealing_optimize(self):
        sa = simulated_annealing.SimulatedAnnealing(100, 0.1)
        solution = [1, 2, 3]
        sa.initialize(solution)
        max_iterations = 10
        sa.optimize(max_iterations)

if __name__ == '__main__':
    unittest.main()
