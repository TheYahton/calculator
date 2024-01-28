import math


VALID_CHARACTERS = set(" 0123456789+-*/()^sin.co")


def add_spaces(s: str) -> str:
    i = 0
    while i < len(s):
        if s[i] in '+-*/)^':
            if s[i-1] != ' ':
                s = s[:i] + ' ' + s[i:]
                i += 1
                
        if s[i] in '+*/(^':
            if s[i+1] != ' ':
                s = s[:i+1] + ' ' + s[i+1:]
                i += 1
        if s[i:i+3] in ('sin', 'cos'):
            if s[i-1] != ' ':
                s = s[:i] + ' ' + s[i:]
                i += 1
            if s[i+3] != ' ':
                s = s[:i+3] + ' ' + s[i+3:]
                i += 1
        i += 1
    return s

def exp_eval(exp: list) -> int:  # exp - expression
    i = 0
    while i < len(exp):
        if exp[i] == 'sin':
            exp[i] = math.sin(exp[i+1])
            exp.pop(i+1)
            i = 0
            continue
        if exp[i] == 'cos':
            exp[i] = math.cos(exp[i+1])
            exp.pop(i+1)
            i = 0
            continue
        i += 1

    i = 0
    while i < len(exp):
        if exp[i] == '^':
            exp[i] = exp[i-1] ** exp[i+1]
            exp.pop(i-1)
            exp.pop(i)
            i = 0
            continue
        i += 1
    i = 0
    while i < len(exp):
        if exp[i] == '*':
            exp[i] = exp[i-1] * exp[i+1]
            exp.pop(i-1)
            exp.pop(i)
            i = 0
            continue
        if exp[i] == '/':
            exp[i] = exp[i-1] / exp[i+1]
            exp.pop(i-1)
            exp.pop(i)
            i = 0
            continue
        i += 1
    i = 0
    while i < len(exp):
        if exp[i] == '+':
            exp[i] = exp[i-1] + exp[i+1]
            exp.pop(i-1)
            exp.pop(i)
            i = 0
            continue
        elif exp[i] == '-':
            exp[i] = exp[i-1] - exp[i+1]
            exp.pop(i-1)
            exp.pop(i)
            i = 0
            continue
        i += 1
    return exp

def metacalc(exp: list) -> int|float:  # exp - expression
    while len(exp) != 1:
        if '(' in exp:
            ioc = 0
            while True:
                io = exp.index('(', ioc)
                ic = exp.index(')')
                if '(' in exp[io+1:ic]:
                    ioc += 1
                    continue
                break
            exp[io:ic+1] = metacalc(exp[io+1:ic])
        else:
            exp = exp_eval(exp)

    return exp

def main(inp: str) -> int|float:
    if inp == "":
        return 0
    if not VALID_CHARACTERS.issuperset(inp):
        raise SyntaxError("Inputted string contains invalid symbols!")

    inp = add_spaces(inp)
    inp = inp.split()

    i = 0
    while i < len(inp):
        try:
            inp[i] = float(inp[i])
            if inp[i] < 0 and isinstance(inp[i-1], int|float):
                inp.insert(i, '+')
                i += 1
            if inp[i] < 0 and inp[i-1] == ')':
                inp.insert(i, '+')
                i += 1
        except ValueError:
            pass
        i += 1

    if inp.count('(') != inp.count(')'):
        raise SyntaxError("number of '(' is not equals to number of ')'")

    return metacalc(inp)[0]

if __name__ == '__main__':
    print("simplecalc v1.1 python edition")
    while True:
        inp = input(">>> ")
        print(main(inp))
