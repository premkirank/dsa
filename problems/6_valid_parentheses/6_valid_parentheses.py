import sys
import os
from functools import reduce

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit
def valid_parentheses(string):
    parentheses_value_map = {"(": 1, ")": -1, "{": 2, "}": -2, "[": 3, "]": -3}
    order_check = []
    
    for parentheses in string:
        value = parentheses_value_map[parentheses]
        if value > 0:
            order_check.append(value)
        else:
            try:
                popped_value = order_check.pop()
            except Exception as _:
                return False
            if abs(value) != popped_value:
                return False

    if len(order_check) != 0:
        return False
    
    return True


if __name__ == "__main__":
    string = "()[]{}"
    string = "(]"
    string = "([)]"
    string = "()"
    string = "]"
    string = "["

    validity = valid_parentheses(string)
    print(validity)
