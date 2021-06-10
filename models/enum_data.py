import enum
gender_values = dict(Male=1, Female=2)
customer_type_values = dict(Priveleged=1, Normal=2)


class EnumData:
    gender = enum.Enum('Gender', gender_values)
    customer_type = enum.Enum('Customer_Type', customer_type_values)
