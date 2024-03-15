#last module main
import curses
import numpy as np
import os

from domain.student import Student
from domain.course import Course
from domain.student_list import StudentsList
from domain.course_list import CoursesList
from input import *
from output import *

student_list = StudentsList()
course_list = CoursesList()
number_students = 0
number_courses = 0

def main(stdscr):
    stdscr.clear()
    global number_students
    global number_courses
    student_list = StudentsList()
    course_list = CoursesList()

    while True:
        stdscr.addstr("""
        Menu:
        0. Exit
        1. Set number of students
        2. Set number of courses
        3. Input student information
        4. Input course information
        5. Input mark for a student for a course
        6. Show students
        7. Show courses
        8. Show student marks
        9. Round down student marks
        10. Sort GPA
        11. Create student data file
        12. Create course data file
        13. Create mark data file
        14. Compress files
        15. Check and load data
        16. Decompress file
        Enter your option (0-16): 
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
            input_students_information(stdscr, student_list, number_students)
        elif option == 4:
            input_courses_information(stdscr, course_list, number_courses)
        elif option == 5:
            input_marks_information(stdscr, student_list, course_list)
        elif option == 6:
            student_list.show_students_list(stdscr)
        elif option == 7:
            course_list.show_courses_list(stdscr)
        elif option == 8:
            show_mark(stdscr, student_list)
        elif option == 9:
            round_down_mark(stdscr, student_list)
        elif option == 10:
            sort_gpa(stdscr, student_list)
        elif option == 11:
            create_student_data_file(student_list)
        elif option == 12:
            create_course_data_file(course_list)
        elif option == 13:
            create_mark_data_file(student_list)
        elif option == 14:
            compress_files()
        elif option == 15:
            check_and_load_data(student_list, course_list)
        elif option == 16:
            decompress_file()
        else:
            stdscr.addstr("\nInvalid input. Please try again!")
            stdscr.addstr("Press any key to close!")
            stdscr.getch()    
            stdscr.clear()
        
        curses.noecho()

if __name__ == "__main__":
    curses.wrapper(main)
