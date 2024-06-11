import unittest
from main import str2digit, sanitaze, tokenize, parse, interprete, calculate
from math import inf, sin

STR2DIGIT_TEST = (("5", 5), ("-6", -6), ("3.65", 3.65), ("3+5.5j", 3 + 5.5j))

SANITAZE_TEST = (("5+3", "5\+3"), ("7**2", "7\*\*2"), ("(5^2)", "\(5\^2\)"))

LEXER_TEST = (
    ("1+1", [1, "+", 1]),
    ("1-1", [1, "-", 1]),
    ("-1+1", [-1, "+", 1]),
    ("-1-1", [-1, "-", 1]),
    ("2*-1", [2, "*", -1]),
)

PARSER_TEST = (([2, "+", 3], [2, 3, "+"]),)


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

    def test_lexer(self):
        for pair in LEXER_TEST:
            self.assertEqual(tokenize(pair[0]), pair[1])

    def test_parser(self):
        for pair in PARSER_TEST:
            self.assertEqual(parse(pair[0]), pair[1])

    def test_calculate(self):
        for pair in CALCULATE_TEST:
            self.assertEqual(calculate(pair[0]), pair[1])
