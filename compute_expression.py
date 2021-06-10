from models.all_of import AllOf
from models.none_of import NoneOf
from models.between import Between
from models.less_than_equal_to import LessThanEqualTo
from models.greater_than_equal_to import GreaterThanEqualTo
from models.less_than import LessThan
from typing import List
from models.exactly_equal import ExactlyEqualTO
from models.greater_than import GreaterThan
from models.logical_and import LogicalAnd
from models.logical_or import LogicalOr


OPERATORS = {'&&': LogicalAnd.get_instance(),
             '>': GreaterThan.get_instance(),
             '(': 1,
             ')': 1,
             '==': ExactlyEqualTO.get_instance(),
             '||': LogicalOr.get_instance(),
             '<': LessThan.get_instance(),
             '>=': GreaterThanEqualTo.get_instance(),
             '<=': LessThanEqualTo.get_instance(),
             'Between': Between.get_instance(),
             'NoneOf': NoneOf.get_instance(),
             'AllOf': AllOf.get_instance()}

PRIORITY = {'&&': LogicalAnd.get_instance().get_precedence(),
            '>': GreaterThan.get_instance().get_precedence(),
            '==': ExactlyEqualTO.get_instance().get_precedence(),
            '||': LogicalOr.get_instance().get_precedence(),
            '<': LessThan.get_instance().get_precedence(),
            '>=': GreaterThanEqualTo.get_instance().get_precedence(),
            '<=': LessThanEqualTo.get_instance().get_precedence(),
            'Between': Between.get_instance().get_precedence(),
            'NoneOf': NoneOf.get_instance().get_precedence(),
            'AllOf': AllOf.get_instance().get_precedence()}


def infix_to_postfix(expression):
    expression = expression.split()
    stack = []
    output = []
    for ch in expression:
        if ch not in OPERATORS:
            output.append(ch)
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return output


def evaluate_postfix_expression(postfix_expression: list, user_data):
    operand_stack = []
    print("POST ", postfix_expression)
    for element in postfix_expression:
        if(element in OPERATORS):
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = OPERATORS[element].calculate_result([op1, op2])
            print("operations ", op1, op2, res)
            operand_stack.append(res)
        else:
            if user_data.get(element, None) is not None:
                element = user_data[element]
            operand_stack.append(element)

    return operand_stack.pop()
