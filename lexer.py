import re
from structs import OPERATORS, FUNCTIONS

def sanitaze(string: str) -> str:
    for symbol in "+*^()":
        string = string.replace(symbol, "\\" + symbol)
    return string


def tokenize(string: str) -> list[str | int | float | complex]:
    """
    Лексер (токенайзер), разбивает строку на лексемы (токены).
    """

    pattern = "(" + sanitaze("|".join(list(FUNCTIONS)+list(OPERATORS)) + "|)|(") + ")"

    # Используем регулярные выражения, чтобы поставить пробелы вокруг операций. Очень удобно после этого сплитнуть строку и получить список недотокенов. (недотокены нуждаются в дополнительном преобразовании в токены)
    string = re.sub(pattern, r" \1 ", string)
    expression = string.split()

    for i, value in enumerate(expression):
        if value in OPERATORS:
            expression[i] = OPERATORS[value]
        elif value in FUNCTIONS:
            expression[i] = FUNCTIONS[value]
        elif value.isdigit():
            expression[i] = int(value)


    return expression
