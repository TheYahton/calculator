#def str2digit(s: str) -> int | float | str:
#    try:
#        return int(s, NUMBER_SYSTEMS.get(s[0:2], 10))
#    except ValueError:
#        try:
#            return float(s)
#        except ValueError:
#            try:
#                return complex(s)
#            except ValueError:
#                return s


def parse(expression) -> list[str | int | float | complex]:
    """
    Алгоритм сортировочной станции (shunting yard algorithm). Переводит инфиксное выражение в постфиксное (RPN, обратная польская запись).
    """

    output = []
    stack = []

    for token in expression:
        if isinstance(token, (int, float, complex)):
            output.append(token)
        elif isinstance(token, tuple):
            while (
                stack
                and stack[-1] != "("
                and token[2] <= stack[-1][2]
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
