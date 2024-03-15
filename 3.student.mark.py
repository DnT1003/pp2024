import math
import numpy as np
import datetime 
import curses

class Person:
    def __init__(self, name, dob):
        self.__name = name 
        self.__dob = dob
    
    def display_info(self):
        return f"Name: {self.__name}, Date of Birth: {self.__dob}"

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

class CoursesList:
    def __init__(self):
        self.__courses = []
    
    def add_course(self, course):
        if isinstance(course, Course):
            self.__courses.append(course)
        else:
            print("Invalid course")
    
    def show_courses_list(self, stdscr):
        stdscr.clear()
        for course in self.__courses:
            stdscr.addstr(course.display_info() + "\n")
        stdscr.addstr("Press any key to close!")
        stdscr.getch()    
        stdscr.clear()

student_list = StudentsList()
course_list = CoursesList()

def set_number_of_students(stdscr):
    stdscr.clear()
    stdscr.addstr("\nNumber of students: ")
    stdscr.refresh()
    curses.echo()
    number_students = int(stdscr.getstr().decode())
    curses.noecho()
    stdscr.clear()
    return number_students

def set_number_of_courses(stdscr):
    stdscr.clear()
    stdscr.addstr("\nNumber of courses: ")
    stdscr.refresh()
    curses.echo()
    number_courses = int(stdscr.getstr().decode())
    curses.noecho()
    stdscr.clear()
    return number_courses

def input_students_information(stdscr):
    stdscr.clear()
    existing_ids = set()  # Set to store existing student IDs
    while len(student_list._StudentsList__students) < number_students:
        stdscr.addstr(f"Student {len(student_list._StudentsList__students) + 1}: ")
        
        # Validate student ID
        while True:
            stdscr.addstr("\nStudent ID: ")
            stdscr.refresh()
            curses.echo()
            s_id = stdscr.getstr().decode()
            curses.noecho()
            if s_id in existing_ids:
                stdscr.addstr("Caution: The entered student ID already exists. Please enter a different ID.\n")
            else:
                existing_ids.add(s_id)
                break

        stdscr.addstr("Student Name: ")
        stdscr.refresh()
        curses.echo()
        s_name = stdscr.getstr().decode()
        curses.noecho()

        # Date of birth input with validation
        while True:
            stdscr.addstr("Student's Date of Birth (YYYY-MM-DD): ")
            stdscr.refresh()
            curses.echo()
            s_dob = stdscr.getstr().decode()
            curses.noecho()
            try:
                datetime.datetime.strptime(s_dob, "%Y-%m-%d")
                break
            except ValueError:
                stdscr.addstr("Invalid date format or out of range. Please enter a valid date.\n")

        standard_student = Student(s_id, s_name, s_dob)
        student_list.add_student(standard_student)
        stdscr.addstr("Input successfully!")
        stdscr.addstr("Press any key to close!")
        stdscr.getch()
        stdscr.clear()

def input_courses_information(stdscr):
    stdscr.clear()
    while len(course_list._CoursesList__courses) < number_courses:
        while True:
            stdscr.addstr(f"Course {len(course_list._CoursesList__courses)+1}: ")
            stdscr.addstr("\nCourse ID: ")
            stdscr.refresh()
            curses.echo()
            c_id = stdscr.getstr().decode()
            curses.noecho()

            stdscr.addstr("Course Name: ")
            stdscr.refresh()
            curses.echo()
            c_name = stdscr.getstr().decode()
            curses.noecho()

            stdscr.addstr("Course Credit: ")
            stdscr.refresh()
            curses.echo()
            c_credit_str = stdscr.getstr().decode()
            curses.noecho()

            try:
                c_credit = int(c_credit_str)
                break
            except ValueError:
                stdscr.clear()
                stdscr.addstr("Please enter a valid integer for Course Credit!\n")

        standard_course = Course(c_id, c_name, c_credit)
        course_list.add_course(standard_course)
        stdscr.addstr("Input successfully!")
        stdscr.addstr("Press any key to close!")
        stdscr.getch()
        stdscr.clear()

def validate_mark_input(stdscr, mark_str):
    try:
        mark = float(mark_str)
        if mark < 0 or mark > 20:
            stdscr.addstr("Warning: Mark should be between 0 and 20. Please try again.\n")
            return False, None
        return True, mark
    except ValueError:
        stdscr.addstr("Warning: Invalid input. Please enter a number for the mark.\n")
        return False, None

def add_mark(stdscr):
    stdscr.clear()
    for student in student_list._StudentsList__students:
        for course in course_list._CoursesList__courses:
            stdscr.addstr(f"Enter the mark of {student.display_info()} for {course.display_info()}: ")
            stdscr.refresh()
            curses.echo()
            mark_input = stdscr.getstr().decode()
            curses.noecho()
            valid, mark = validate_mark_input(stdscr, mark_input)
            if valid:
                student.input_marks(course, mark)
            else:
                # Clear the input line
                stdscr.move(stdscr.getyx()[0] - 1, 0)
                stdscr.clrtoeol()
            stdscr.clear()

def show_mark(stdscr):
    stdscr.clear()
    for student in student_list._StudentsList__students:
        stdscr.addstr(f"\n{student.display_info()}\n")
        stdscr.addstr(student.list_marks())
    stdscr.addstr("Press any key to close!")
    stdscr.getch()
    stdscr.clear()

def round_down_mark(stdscr):
    stdscr.clear()
    for student in student_list._StudentsList__students:
        stdscr.addstr(f"{student.display_info()}\n")
        stdscr.addstr(student.list_marks())
        stdscr.addstr("Press any key to see the next student!")
        stdscr.getch()    
        stdscr.clear()

def sort_gpa(stdscr):
    stdscr.clear()
    dtype = [('Name', 'U10'), ('GPA', float)]
    students = np.array([], dtype=dtype)
    for student in student_list._StudentsList__students:
        marks = student.show_mark()
        total_weighted_marks = 0
        total_credits = 0
        for course, mark in marks.items():
            credits = course.show_credit()
            total_weighted_marks += mark * credits
            total_credits += credits
        if total_credits == 0:
            gpa = 0
        else:
            gpa = total_weighted_marks / total_credits
        students = np.append(students, np.array([(student.show_name(), gpa)], dtype))
    student_sort = np.sort(students, order='GPA')[::-1]
    stdscr.addstr("GPA Leaderboard:\n")
    for student in student_sort:
        stdscr.addstr(f"Name: {student['Name']}, GPA: {student['GPA']:.2f}\n")
    stdscr.addstr("Press any key to close!")
    stdscr.getch()    
    stdscr.clear()

def main(stdscr):
    stdscr.clear()
    global number_students
    global number_courses

    while True:
        stdscr.addstr("""
    0. Exit
    1. Input the total number of students.    
    2. Input the total number of courses.          
    3. Input student information. 
    4. Input course information.
    5. Input mark for student for a course.
    6. Show the students.
    7. Show the courses.
    8. Show the students' mark.
    9. Round-down students' mark.
    10. Sort GPA
    Input your option: 
    """)
        stdscr.refresh()
        option_str = stdscr.getstr().decode()
        option = int(option_str)
        curses.echo()
        
        if option == 0:
            break
        elif option == 1:
            number_students = set_number_of_students(stdscr)
        elif option == 2:
            number_courses = set_number_of_courses(stdscr)
        elif option == 3:
            input_students_information(stdscr)
        elif option == 4:
            input_courses_information(stdscr)
        elif option == 5:
            add_mark(stdscr)
        elif option == 6:
            student_list.show_students_list(stdscr)
        elif option == 7:
            course_list.show_courses_list(stdscr)
        elif option == 8:
            show_mark(stdscr)
        elif option == 9:
            round_down_mark(stdscr)
        elif option == 10:
            sort_gpa(stdscr)
        else:
            stdscr.addstr("\nInvalid input. Please try again!")
            stdscr.addstr("Press any key to close!")
            stdscr.getch()    
            stdscr.clear()
        
        curses.noecho()

if __name__ == "__main__":
    curses.wrapper(main)
