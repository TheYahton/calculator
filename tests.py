import unittest
from lexer import sanitaze, tokenize
from parser import parse
from interpreter import interprete
from main import calculate
from math import inf, sin
from structs import OPERATORS as OPS


class TestCase(unittest.TestCase):
    def test_sanitaze(self):
        self.assertEqual(sanitaze("5+3"), "5\+3")
        self.assertEqual(sanitaze("7**2"), "7\*\*2")
        self.assertEqual(sanitaze("(5^2)"), "\(5\^2\)")

    def test_lexer(self):
        self.assertEqual(tokenize("1+1"), [1, OPS["+"], 1])
        self.assertEqual(tokenize("1-1"), [1, OPS["-"], 1])
        self.assertEqual(tokenize("-1+1"), [-1, OPS["+"], 1])
        self.assertEqual(tokenize("-1-1"), [-1, OPS["-"], 1])
        self.assertEqual(tokenize("2*-1"), [2, OPS["*"], -1])

    def test_parser(self):
        self.assertEqual(parse(tokenize("2 + 3")), tokenize("2 3 +"))

    def test_calculate(self):
        self.assertEqual(calculate("1+8"), 9)
        self.assertEqual(calculate("1-5"), -4)
        self.assertEqual(calculate("2*-1"), -2)
        self.assertEqual(calculate("10j/50j"), 10j / 50j),
        self.assertEqual(calculate("10e5**2"), 10e5**2)
        self.assertEqual(calculate("2*sin(3.14)-74"), 2 * sin(3.14) - 74)
