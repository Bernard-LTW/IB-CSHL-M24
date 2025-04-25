#2023-11-28 Quiz095
import sys

sys.path.append('../Year2')

from Lessons import adts
def is_balanced_parenthesis(input_str:str):
    stack = adts.stack()
    open_parenthesis = "([{"
    close_parenthesis = ")]}"
    for i in input_str:
        if i in open_parenthesis:
            stack.push(i)
        elif i in close_parenthesis:
            if stack.isEmpty():
                return False
            else:
                if open_parenthesis.index(stack.pop()) != close_parenthesis.index(i):
                    return False
    return stack.isEmpty()


def is_balanced_parenthesis2(input_str:str):
    a = input_str.count('(') != input_str.count(')')
    b = input_str.count('[') != input_str.count(']')
    c = input_str.count('{') != input_str.count('}')
    return not (a or b or c)