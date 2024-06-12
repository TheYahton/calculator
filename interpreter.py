def interprete(expression: list) -> int | float:
    """
    Типичная стековая машина.
    """

    stack = []
    for token in expression:
        print(f"stack=")
        if isinstance(token, tuple):
            #  popping the required number of arguments onto the stack
            args = [stack.pop() for _ in range(token[1])]
            #  applying the operation and appending the result back to the stack
            stack.append(token[0](*reversed(args)))
        else:
            stack.append(token)
    return stack.pop()
