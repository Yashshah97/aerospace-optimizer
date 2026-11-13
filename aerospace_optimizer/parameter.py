"""
Module for data structures and methods related to parameter handling.

This module provides classes and functions for defining parameters with their bounds,
constraints, and other relevant attributes.
"""

class Parameter:
    """
    Represents a single parameter in the optimization problem.

    Attributes:
        name (str): Name of the parameter.
        lower_bound (float): Lower bound of the parameter's range.
        upper_bound (float): Upper bound of the parameter's range.
        constraint (callable, optional): Constraint function for the parameter.
    """

    def __init__(self, name: str, lower_bound: float, upper_bound: float,
                 constraint=None):
        """
        Initializes a Parameter instance.

        Args:
            name (str): Name of the parameter.
            lower_bound (float): Lower bound of the parameter's range.
            upper_bound (float): Upper bound of the parameter's range.
            constraint (callable, optional): Constraint function for the parameter.
        """
        self.name = name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.constraint = constraint

    @property
    def bounds(self):
        """Returns a tuple containing the parameter's bounds."""
        return (self.lower_bound, self.upper_bound)


class ParameterSet:
    """
    Represents a set of parameters in the optimization problem.

    Attributes:
        parameters (dict): Dictionary mapping parameter names to their instances.
    """

    def __init__(self):
        """
        Initializes an empty ParameterSet instance.
        """
        self.parameters = {}

    def add_parameter(self, name: str, lower_bound: float, upper_bound: float,
                      constraint=None):
        """
        Adds a parameter to the set.

        Args:
            name (str): Name of the parameter.
            lower_bound (float): Lower bound of the parameter's range.
            upper_bound (float): Upper bound of the parameter's range.
            constraint (callable, optional): Constraint function for the parameter.
        """
        self.parameters[name] = Parameter(name, lower_bound, upper_bound,
                                          constraint)

    def get_parameter(self, name: str):
        """Returns a parameter instance by its name."""
        return self.parameters.get(name)
