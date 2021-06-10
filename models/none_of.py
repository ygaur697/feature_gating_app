from utils import convert_string_to_int
from Exceptions.InvalidOperandCount import InvalidOperandCount

class NoneOf:
    precedence = None
    none_of = None    
    operand_count = None

    def __init__(self) -> None:
        self.precedence = 5       
        self.operand_count = 2

    @staticmethod
    def get_instance():
        if NoneOf.none_of == None:
            NoneOf.none_of = NoneOf()
        return NoneOf.none_of

    def get_operand_count(self):
        return self.operand_count

    def get_precedence(self):
        return self.precedence   

    def calculate_result(self, operands: list()) -> bool:
        if len(operands) != self.operand_count:
            raise InvalidOperandCount

        operand_1 = operands[0]
        operand_2 = convert_string_to_int(operands[1])
        for operand in operand_2:            
                if operand == operand_1:
                    return False
        return True
