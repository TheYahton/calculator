import math
import operator as op
import enum

VALID_CHARACTERS = set(
    " 0123456789+-*/()^.>==<%E sin cos tan cot sqrt ln pi e 0x 0b 0o ABCDEF abcdef j"
)

NUMBER_SYSTEMS = {
    "0b": 2,
    "0o": 8,
    "0x": 16,
}

OPERATORS = {
    "==": (op.eq, 2, 0),
    "**": (op.pow, 2, 3),
    "//": (op.floordiv, 2, 2),
    "<<": (op.lshift, 2, 2),
    ">>": (op.rshift, 2, 2),
    ">=": (op.ge, 2, 0),
    "<=": (op.le, 2, 0),
    ">": (op.gt, 2, 0),
    "<": (op.lt, 2, 0),
    "+": (op.add, 2, 1),
    "-": (op.sub, 2, 1),
    "*": (op.mul, 2, 2),
    "/": (op.truediv, 2, 2),
    "%": (op.mod, 2, 2),
    "^": (op.xor, 2, 3),
}

FUNCTIONS = {
    "sqrt": (math.sqrt, 1, 4),
    "sin": (math.sin, 1, 4),
    "cos": (math.cos, 1, 4),
    "tan": (math.tan, 1, 4),
    "cot": (lambda a: 1 / math.tan(a), 1, 4),
    "ln": (math.log, 1, 4),
}

class Token(enum.Enum):
    PLUS = 1
    MINUS = 2
    ASTERISK = 3
    SLASH = 4
