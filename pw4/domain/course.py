from domain.student import Student 

class Course:
    def __init__(self, id, name, credit):
        self.__name = name
        self.__id = id
        self.__credit = credit
        self.__students = {}

    def show_name(self):
        return self.__name
    
    def show_id(self):
        return self.__id
    
    def show_credit(self):
        return self.__credit
    
    def add_student(self, student):
        self.__students[student._Student__id] = student  

    def list_students(self):
        info = f"Course: {self.__name}\n"
        if self.__students:
            for student_id, student in self.__students.items():
                info += student.list_marks()
                info += "\n"
        else:
            info += "No students enrolled.\n"
        return info

    def display_info(self):
        return f"Course Name: {self.__name}"