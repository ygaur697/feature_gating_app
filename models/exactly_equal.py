from utils import convert_string_to_int
from Exceptions.InvalidOperandCount import InvalidOperandCount

class ExactlyEqualTO:
    precedence = None
    exactly_equal_to = None    
    operand_count = None

    def __init__(self) -> None:
        self.precedence = 4      
        self.operand_count = 2

    @staticmethod
    def get_instance():
        if ExactlyEqualTO.exactly_equal_to == None:
            ExactlyEqualTO.exactly_equal_to = ExactlyEqualTO()
        return ExactlyEqualTO.exactly_equal_to

    def get_operand_count(self):
        return self.operand_count

    def get_precedence(self):
        return self.precedence  

    def calculate_result(self, operands: list()) -> bool:
        if len(operands) != self.operand_count:
            raise InvalidOperandCount

        if type(operands[0]) is int:
            operand_2 = convert_string_to_int(operands[1])
            return operands[0] == operand_2

        if (type(operands[0]) == str and type(operands[1]) == str):
            return operands[0].lower() == operands[1].lower()
