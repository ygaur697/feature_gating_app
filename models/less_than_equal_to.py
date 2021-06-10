from Exceptions.InvalidTypeOfOperand import InvalidTypeOfOperand
from utils import convert_string_to_int
from Exceptions.InvalidOperandCount import InvalidOperandCount

class LessThanEqualTo:
    precedence = None
    less_than_equal_to = None   
    operand_count = None

    def __init__(self) -> None:
        self.precedence = 4       
        self.operand_count = 2

    @staticmethod
    def get_instance():
        if LessThanEqualTo.less_than_equal_to == None:
            LessThanEqualTo.less_than_equal_to = LessThanEqualTo()
        return LessThanEqualTo.less_than_equal_to

    def get_operand_count(self):
        return self.operand_count

    def get_precedence(self):
        return self.precedence  

    def calculate_result(self, operands: list()) -> bool:
        if len(operands) != self.operand_count:
           raise InvalidOperandCount
        operand_1 = operands[0]
        if type(operand_1) is not int:
            operand_1 = convert_string_to_int(operand_1)

        operand_2 = convert_string_to_int(operands[1])
        if type(operand_2) is not int:
            operand_2 = convert_string_to_int(operand_2)

        if operand_1 is not None and operand_2 is not None:
            return operand_1 < operand_2

        raise InvalidTypeOfOperand