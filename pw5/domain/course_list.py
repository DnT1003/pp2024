from domain.course import Course
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