from Exceptions.InvalidOperandCount import InvalidOperandCount

class LogicalAnd:
    precedence = None
    logical_and = None
    operand_count = None

    def __init__(self) -> None:
        self.precedence = 2
        self.operand_count = 2

    @staticmethod
    def get_instance():
        if LogicalAnd.logical_and == None:
            LogicalAnd.logical_and = LogicalAnd()
        return LogicalAnd.logical_and

    def get_operand_count(self):
        return self.operand_count

    def get_precedence(self):
        return self.precedence

    def calculate_result(self, operands: list()) -> bool:
        if len(operands) != self.operand_count:
           raise InvalidOperandCount

        for operand in operands:
            if(type(operand) != bool):
                print("Throw exception here for unsupported operand")
            if(operand == False):
                return False
        return True
