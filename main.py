from lexer import tokenize
from parser import parse
from interpreter import interprete
from structs import VALID_CHARACTERS


def calculate(string: str) -> float:
    if string == "":
        return 0
    if not VALID_CHARACTERS.issuperset(string):
        raise SyntaxError("The entered string contains invalid characters!")
    
    expression = tokenize(string)
    ast = parse(expression)
    result = interprete(ast)

    return result


if __name__ == "__main__":
    print("serpentinum calculatio")
    while True:
        print(calculate(input(">>> ")))
