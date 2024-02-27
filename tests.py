import unittest
from main import calculate, tokenize, evaluate_rpn, infix_to_rpn
from math import inf, sin

TOKENIZE_TEST = (
    {"arg": "1+1", "res": [1, "+", 1]},
    {"arg": "1-1", "res": [1, "-", 1]},
    {"arg": "-1+1", "res": [-1, "+", 1]},
    {"arg": "-1-1", "res": [-1, "-", 1]},
    {"arg": "2*-1", "res": [2, "*", -1]},
)

CALCULATE_TEST = (
    {"arg": "1+1", "res": 2},
    {"arg": "1-1", "res": 0},
    {"arg": "-1+1", "res": 0},
    {"arg": "-1-1", "res": -2},
    {"arg": "2*-1", "res": -2},
    {"arg": "1/0", "res": inf},
    {"arg": "10j", "res": 10j},
    {"arg": "10e5", "res": 10e5},
    {"arg": "sin(3.14)", "res": sin(3.14)},
)

class TestCase(unittest.TestCase):
    def test_tokenize(self):
        for pair in TOKENIZE_TEST:
            self.assertEqual(tokenize(pair["arg"]), pair["res"])
    
    def test_calculate(self):
        for pair in CALCULATE_TEST:
            self.assertEqual(calculate(pair["arg"]), pair["res"])
