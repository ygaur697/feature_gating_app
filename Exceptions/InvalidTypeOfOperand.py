class InvalidTypeOfOperand(Exception):
    def __init__(self, message = "You have entered invalid type of Operands, Please refer docs"):
        self.message = message
        super().__init__(self.message)
