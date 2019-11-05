#!/usr/bin/env python3

import operator
from colorama import *


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if (result % 2 == 0):
            print("Result", Fore.BLUE + str(result) + Style.RESET_ALL)
        else:
            print("Result", Fore.RED + str(result) + Style.RESET_ALL)

if __name__ == '__main__':
    main()
