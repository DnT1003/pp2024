
class Person:
    def __init__(self, name, dob):
        self.__name = name 
        self.__dob = dob
    
    def display_info(self):
        return f"Name: {self.__name}, Date of Birth: {self.__dob}"
