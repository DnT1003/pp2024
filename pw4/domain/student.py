from domain.person import Person

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(name, dob)
        self.__id = id
        self.__marks = {}

    def input_marks(self, course, mark):
        self.__marks[course] = mark

    def list_marks(self):
        info = super().display_info() + "\n"
        if self.__marks:
            info += "Marks:\n"
            for course, mark in self.__marks.items():
                info += f"  {course}: {mark}\n"
        else:
            info += "No marks available.\n"
        return info