import unittest
from main import str2digit, sanitaze, tokenize, infix2rpn, evaluate_rpn, calculate
from math import inf, sin

STR2DIGIT_TEST = (("5", 5), ("-6", -6), ("3.65", 3.65), ("3+5.5j", 3 + 5.5j))

SANITAZE_TEST = (("5+3", "5\+3"), ("7**2", "7\*\*2"), ("(5^2)", "\(5\^2\)"))

TOKENIZE_TEST = (
    ("1+1", [1, "+", 1]),
    ("1-1", [1, "-", 1]),
    ("-1+1", [-1, "+", 1]),
    ("-1-1", [-1, "-", 1]),
    ("2*-1", [2, "*", -1]),
)

INFIX2RPN_TEST = (([2, "+", 3], [2, 3, "+"]),)


CALCULATE_TEST = (
    ("1+8", 9),
    ("1-5", -4),
    ("2*-1", -2),
    ("10j/50j", 10j / 50j),
    ("10e5**2", 10e5**2),
    ("2*sin(3.14)-74", 2 * sin(3.14) - 74),
)


class TestCase(unittest.TestCase):
    def test_str2digit(self):
        for pair in STR2DIGIT_TEST:
            self.assertEqual(str2digit(pair[0]), pair[1])

    def test_sanitaze(self):
        for pair in SANITAZE_TEST:
            self.assertEqual(sanitaze(pair[0]), pair[1])

    def test_tokenize(self):
        for pair in TOKENIZE_TEST:
            self.assertEqual(tokenize(pair[0]), pair[1])

    def test_infix2rpn(self):
        for pair in INFIX2RPN_TEST:
            self.assertEqual(infix2rpn(pair[0]), pair[1])

    def test_calculate(self):
        for pair in CALCULATE_TEST:
            self.assertEqual(calculate(pair[0]), pair[1])
