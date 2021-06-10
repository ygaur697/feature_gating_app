import enum
from models.enum_data import EnumData
class User:
    name:str 
    email:str 
    phone:int
    gender:EnumData.gender
    past_order_amount:int

    def __init__(self, name:str, email:str, phone:int, gender:EnumData.gender, past_order_amount:int, age: int):
        self.name = name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.past_order_amount = past_order_amount
        self.age = age
