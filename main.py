import math
import re
import operator as op


VALID_CHARACTERS = set(
    " 0123456789+-*/()^.>==<%E sin cos tan cot sqrt ln pi e 0x 0b 0o ABCDEF abcdef j"
)

NUMBER_SYSTEMS = {
    "0b": 2,
    "0o": 8,
    "0x": 16,
}

OPERATIONS = {
    "sqrt": (math.sqrt, 1, 4),
    "sin": (math.sin, 1, 4),
    "cos": (math.cos, 1, 4),
    "tan": (math.tan, 1, 4),
    "cot": (lambda a: 1 / math.tan(a), 1, 4),
    "ln": (math.log, 1, 4),
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


def str2digit(s: str) -> int | float | str:
    try:
        return int(s, NUMBER_SYSTEMS.get(s[0:2], 10))
    except ValueError:
        try:
            return float(s)
        except ValueError:
            try:
                return complex(s)
            except ValueError:
                return s


def sanitaze(string: str) -> str:
    for symbol in "+*^()":
        string = string.replace(symbol, "\\" + symbol)
    return string


def tokenize(string: str) -> list[str | int | float | complex]:
    pattern = "(" + sanitaze("|".join(OPERATIONS) + "|)|(") + ")"
    # using regular expressions to add spaces between operation characters
    string = re.sub(pattern, r" \1 ", string)

    expression = string.split()
    expression = list(map(str2digit, expression))

    for i, val in enumerate(expression):
        if (
            val == "-"
            and (not isinstance(expression[i - 1], (int, float)) or i == 0)
            and not expression[i - 1] == ")"
        ):
            expression[i + 1] = -expression[i + 1]
            expression.pop(i)

    return expression


def infix2rpn(expression) -> list[str | int | float | complex]:
    output = []
    stack = []

    for token in expression:
        if isinstance(token, (int, float, complex)):
            output.append(token)
        elif token in OPERATIONS:
            while (
                stack
                and stack[-1] != "("
                and OPERATIONS[token][2] <= OPERATIONS.get(stack[-1], [0, 0, 0])[2]
            ):
                output.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return output


def evaluate_rpn(expression: list) -> int | float:
    stack = []
    for token in expression:
        if token in OPERATIONS:
            #  popping the required number of arguments onto the stack
            args = [stack.pop() for _ in range(OPERATIONS[token][1])]
            #  applying the operation and appending the result back to the stack
            stack.append(OPERATIONS[token][0](*reversed(args)))
        else:
            stack.append(token)
    return stack.pop()


def calculate(string: str) -> float:
    if string == "":
        return 0
    if not VALID_CHARACTERS.issuperset(string):
        raise SyntaxError("The entered string contains invalid characters!")

    expression = tokenize(string)
    expression = infix2rpn(expression)
    result = evaluate_rpn(expression)

    return result


if __name__ == "__main__":
    print("serpentinum calculatio")
    while True:
        print(calculate(input(">>> ")))
