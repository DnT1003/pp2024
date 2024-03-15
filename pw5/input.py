
import os
import gzip

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

def input_marks_information(stdscr, student_list, course_list):
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
                stdscr.move(stdscr.getyx()[0] - 1, 0)
                stdscr.clrtoeol()
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

def create_student_data_file(student_list):
    with open("student.txt", "w") as file:
        for student in student_list._StudentsList__students:
            file.write(f"{student._Student__id},{student._Person__name},{student._Person__dob}\n")

def create_course_data_file(course_list):
    with open("course.txt", "w") as file:
        for course in course_list._CoursesList__courses:
            file.write(f"{course._Course__id},{course._Course__name},{course._Course__credit}\n")

def create_mark_data_file(student_list):
    with open("mark.txt", "w") as file:
        for student in student_list._StudentsList__students:
            for course, mark in student._Student__marks.items():
                file.write(f"{student._Student__id},{course._Course__id},{mark}\n")

def compress_files():
    with open("student.txt", "rb") as f_student, open("course.txt", "rb") as f_course, open("mark.txt", "rb") as f_mark:
        with gzip.open("student.dat", "wb") as f_out:
            f_out.write(f_student.read())
            f_out.write(f_course.read())
            f_out.write(f_mark.read())

def check_and_load_data(student_list, course_list):
    if os.path.exists("student.dat"):
        with gzip.open("student.dat", "rb") as f_in:
            data = f_in.read().splitlines()
            num_students = len(student_list._StudentsList__students)
            num_courses = len(course_list._CoursesList__courses)
            # Assuming each line corresponds to a record
            for i in range(num_students):
                s_id, s_name, s_dob = data[i].decode().split(',')
                student = Student(s_id, s_name, s_dob)
                student_list.add_student(student)
            for j in range(num_students, num_students + num_courses):
                c_id, c_name, c_credit = data[j].decode().split(',')
                course = Course(c_id, c_name, int(c_credit))
                course_list.add_course(course)
            for k in range(num_students + num_courses, len(data)):
                s_id, c_id, mark = data[k].decode().split(',')
                student = student_list.get_student_by_id(s_id)
                course = course_list.get_course_by_id(c_id)
                student.input_marks(course, float(mark))

def decompress_file():
    with gzip.open("student.dat", "rb") as f_in:
        data = f_in.read().splitlines()
        with open("student.txt", "wb") as f_student, open("course.txt", "wb") as f_course, open("mark.txt", "wb") as f_mark:
            num_students = len(student_list._StudentsList__students)
            num_courses = len(course_list._CoursesList__courses)
            for i in range(num_students):
                f_student.write(data[i] + b'\n')
            for j in range(num_students, num_students + num_courses):
                f_course.write(data[j] + b'\n')
            for k in range(num_students + num_courses, len(data)):
                f_mark.write(data[k] + b'\n')

student_list = StudentsList()
course_list = CoursesList()