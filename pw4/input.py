from domain.student import Student
from domain.course import Course
from domain.student_list import StudentsList
from domain.course_list import CoursesList
import datetime 
import curses

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

def input_students_information(stdscr, student_list, number_students):
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
def input_courses_information(stdscr, course_list, number_courses):
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
   
student_list = StudentsList()
course_list = CoursesList()
number_students = 0
number_courses = 0