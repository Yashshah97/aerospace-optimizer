"""
Aerospace Parameter Optimizer - Main optimizer class.

This module implements the main optimizer class with various search strategies.
"""

class Optimizer:
    """
    Base class for all optimization algorithms.

    Attributes:
        bounds (list): List of tuples containing lower and upper bounds for each parameter.
        strategy (str): Optimization strategy to use (grid, random, annealing).
    """

    def __init__(self, bounds, strategy):
        self.bounds = bounds
        self.strategy = strategy

    def optimize(self, objective_func):
        """
        Run the optimization algorithm.

        Args:
            objective_func: Function to be optimized.

        Returns:
            Best parameters found.
        """
        raise NotImplementedError("Subclass must implement this method")

class GridOptimizer(Optimizer):
    """
    Grid search optimization strategy.

    Attributes:
        None

    Methods:
        optimize: Run the grid search algorithm.
    """

    def optimize(self, objective_func):
        import itertools
        best_params = None
        best_value = float('inf')
        for params in itertools.product(*[range(b[0], b[1] + 1) for b in self.bounds]):
            value = objective_func(params)
            if value < best_value:
                best_value = value
                best_params = params
        return best_params

class RandomOptimizer(Optimizer):
    """
    Random search optimization strategy.

    Attributes:
        None

    Methods:
        optimize: Run the random search algorithm.
    """

    def __init__(self, bounds, strategy, num_samples=1000):
        super().__init__(bounds, strategy)
        self.num_samples = num_samples

    def optimize(self, objective_func):
        import numpy as np
        best_params = None
        best_value = float('inf')
        for _ in range(self.num_samples):
            params = [np.random.randint(b[0], b[1] + 1) for b in self.bounds]
            value = objective_func(params)
            if value < best_value:
                best_value = value
                best_params = params
        return best_params

class AnnealingOptimizer(Optimizer):
    """
    Simulated annealing optimization strategy.

    Attributes:
        None

    Methods:
        optimize: Run the simulated annealing algorithm.
    """

    def __init__(self, bounds, strategy, initial_temp=1000, cooling_rate=0.99):
        super().__init__(bounds, strategy)
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate

    def optimize(self, objective_func):
        import numpy as np
        best_params = None
        best_value = float('inf')
        current_params = [np.random.randint(b[0], b[1] + 1) for b in self.bounds]
        temp = self.initial_temp
        while temp > 1:
            value = objective_func(current_params)
            if value < best_value:
                best_value = value
                best_params = current_params[:]
            new_params = [np.random.randint(b[0], b[1] + 1) for b in self.bounds]
            delta = objective_func(new_params) - value
            if delta > 0 or np.random.rand() < np.exp(delta / temp):
                current_params = new_params
            temp *= self.cooling_rate
        return best_params
