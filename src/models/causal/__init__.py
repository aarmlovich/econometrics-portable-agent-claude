"""Causal inference methods and identification strategies."""

from .diff_in_diff import DifferenceInDifferences
from .regression_discontinuity import RegressionDiscontinuity
from .matching import Matching
from .instrumental_variables import InstrumentalVariables

__all__ = [
    'DifferenceInDifferences',
    'RegressionDiscontinuity',
    'Matching',
    'InstrumentalVariables',
]
