from domain.student import Student
class StudentsList:
    def __init__(self):
        self.__students = []
    
    def add_student(self, student):
        if isinstance(student, Student):
            self.__students.append(student)
        else:
            print("Invalid student")
    
    def show_students_list(self, stdscr):
        stdscr.clear()
        for student in self.__students:
            stdscr.addstr(student.display_info() + "\n")
        stdscr.addstr("Press any key to close!")
        stdscr.getch()    
        stdscr.clear()