from Exceptions.InvalidTypeOfOperand import InvalidTypeOfOperand
from Exceptions.InvalidOperandCount import InvalidOperandCount

class LogicalOr:
    precedence = None
    logical_or = None    
    operand_count = None

    def __init__(self) -> None:
        self.precedence = 1       
        self.operand_count = 2

    @staticmethod
    def get_instance():
        if LogicalOr.logical_or == None:
            LogicalOr.logical_or = LogicalOr()
        return LogicalOr.logical_or

    def get_operand_count(self):
        return self.operand_count

    def get_precedence(self):
        return self.precedence   

    def calculate_result(self, operands: list()) -> bool:
        if len(operands) != self.operand_count:
            raise InvalidOperandCount

        for operand in operands:
            if(type(operand) != bool):
                raise InvalidTypeOfOperand
            if(operand == True):
                return True
        return False
