import math
import re


VALID_CHARACTERS = set(" 0123456789+-*/()^.sin cos tan cot sqrt ln")

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

def add_spaces(s: str) -> str:
    #  using regular expressions to add spaces between operation characters
    s = re.sub(r'(\+|-^d|\*|/|\^|\(|\))', r' \1 ', s)
    s = re.sub(r'(sin|cos|tg|ctg|sqrt|ln)', r' \1 ', s)
    return s

def evaluate_rpn(expression: list) -> float:
    stack = []
    for token in expression:
        if token in OPERATIONS:
            #  popping the required number of arguments onto the stack
            args = [stack.pop() for _ in range(OPERATIONS[token][1])]
            #  applying the operation and appending the result back to the stack
            stack.append(OPERATIONS[token][0](*reversed(args)))
        else:
            stack.append(float(token))
    return stack.pop()

def infix_to_rpn(expression):
    output = []
    stack = []
    
    for token in expression:
        if token.replace("-", "", 1).replace(".", "", 1).isdigit():
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

def main(string: str) -> int|float:
    if string == "":
        return 0
    if not VALID_CHARACTERS.issuperset(string):
        raise SyntaxError("The entered string contains invalid characters!")

    exp = add_spaces(string).split()
    exp = infix_to_rpn(exp)
    result = evaluate_rpn(exp)

    return result

if __name__ == '__main__':
    print("simplecalc v1 python edition")
    while True:
        print(main(input(">>> ")))
