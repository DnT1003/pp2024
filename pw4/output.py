import curses
import numpy as np
import math
from domain.student import Student
from domain.course import Course
from domain.student_list import StudentsList
from domain.course_list import CoursesList

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

def add_mark(stdscr, student_list, course_list):
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

def show_mark(stdscr, student_list):
    stdscr.clear()
    for student in student_list._StudentsList__students:
        stdscr.addstr(f"\n{student.display_info()}\n")
        stdscr.addstr(student.list_marks())
    stdscr.addstr("Press any key to close!")
    stdscr.getch()
    stdscr.clear()

def round_down_mark(stdscr, student_list):
    stdscr.clear()
    for student in student_list._StudentsList__students:
        stdscr.addstr(f"{student.display_info()}\n")
        stdscr.addstr(student.list_marks())
        stdscr.addstr("Press any key to see the next student!")
        stdscr.getch()    
        stdscr.clear()

def sort_gpa(stdscr, student_list):
    stdscr.clear()
    dtype = [('Name', 'U10'), ('GPA', float)]
    students = np.array([], dtype=dtype)
    for student in student_list._StudentsList__students:
        marks = student.list_marks() 
        total_weighted_marks = 0
        total_credits = 0
        for course, mark in student._Student__marks.items():
            credits = course.show_credit()
            total_weighted_marks += mark * credits
            total_credits += credits
        if total_credits == 0:
            gpa = 0
        else:
            gpa = total_weighted_marks / total_credits
        students = np.append(students, np.array([(student.display_info(), gpa)], dtype))
    student_sort = np.sort(students, order='GPA')[::-1]
    stdscr.addstr("GPA Leaderboard:\n")
    for student in student_sort:
        stdscr.addstr(f"Name: {student['Name']}, GPA: {student['GPA']:.2f}\n")
    stdscr.addstr("Press any key to close!")
    stdscr.getch()    
    stdscr.clear()

student_list = StudentsList()
course_list = CoursesList()
number_students = 0
number_courses = 0
