import math
import re


VALID_CHARACTERS = set(" 0123456789+-*/()^.sin cos tan cot sqrt ln pi e x b ABCDEFabcdef")

NUMBER_SYSTEMS = {
    '0b': (lambda s: int(s, base=2)),
    '0o': (lambda s: int(s, base=8)),
    '0x': (lambda s: int(s, base=16)),
}

OPERATIONS = {
    '+': (lambda a, b: a + b, 2, 1),
    '-': (lambda a, b: a - b, 2, 1),
    '*': (lambda a, b: a * b, 2, 2),
    '/': (lambda a, b: a / b, 2, 2),
    '^': (lambda a, b: a ** b, 2, 3),
    'sin': (lambda a: math.sin(a), 1, 4),
    'cos': (lambda a: math.cos(a), 1, 4),
    'tan': (lambda a: math.tan(a), 1, 4),
    'cot': (lambda a: 1 / math.tan(a), 1, 4),
    'sqrt': (lambda a: math.sqrt(a), 1, 4),
    'ln': (lambda a: math.log(a), 1, 4),
}

def digit(s: str) -> int|float|str:
    try:
        return NUMBER_SYSTEMS.get(s[0:2], lambda s: float(s))(s)
    except ValueError:
        return s

def tokenize(s: str) -> list:
    # replace constants with values
    s = s.replace("pi", str(math.pi)).replace("e", str(math.e))

    # using regular expressions to add spaces between operation characters
    s = re.sub(r'(\+|-|\*|/|\^|\(|\))', r' \1 ', s)
    s = re.sub(r'(sin|cos|tg|ctg|sqrt|ln)', r' \1 ', s)

    expression = s.split()
    expression = list(map(digit, expression))

    for i, val in enumerate(expression):
        if val == '-' and (not isinstance(expression[i-1], (int, float)) or i == 0):
            expression[i+1] = -expression[i+1]
            expression.pop(i)

    return expression

def evaluate_rpn(expression: list) -> float:
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

def infix_to_rpn(expression) -> list:
    output = []
    stack = []
    
    for token in expression:
        if isinstance(token, (int, float)):
            output.append(token)
        elif token in OPERATIONS:
            while stack and stack[-1] != '(' and OPERATIONS[token][2] <= OPERATIONS.get(stack[-1], [0, 0, 0])[2]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    
    while stack:
        output.append(stack.pop())
    
    return output

def calculate(string: str) -> float:
    if string == "":
        return 0
    if not VALID_CHARACTERS.issuperset(string):
        raise SyntaxError("The entered string contains invalid characters!")

    exp = tokenize(string)
    exp = infix_to_rpn(exp)
    result = evaluate_rpn(exp)

    return result

if __name__ == '__main__':
    print("serpentinum calculatio")
    while True:
        print(calculate(input(">>> ")))
