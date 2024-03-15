import datetime

class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def show_student_id(self):
        return self.__id
    
    def show_student_name(self):
        return self.__name
    
    def show_dob(self):
        return self.__dob

class StudentArray:
    def __init__(self):
        self.__info = []
        
    def show_student_info(self):
        return self.__info

class Course:
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def show_course_id(self):
        return self.__id
    
    def show_course_name(self):
        return self.__name

    def show_credit(self):
        return self.__credit   

class CourseArray:
    def __init__(self):
        self.__info = []
        
    def show_course_info(self):
        return self.__info

class Mark:
    def __init__(self, student_id, course_id, mark):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__mark = mark

    def show_mark_student_id(self):
        return self.__student_id
    
    def show_mark_course_id(self):
        return self.__course_id
    
    def show_mark(self):
        return self.__mark
    
def loop_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                return number
            else:
                print("Invalid value. Please enter a non-negative number.")
        except ValueError:
            print("Error: value must be an integer. Please try again.")

def add_items(cls, args, info):
    number_of_variables = int(input(f"Enter the number of {args} you want to add: "))

    for item in input_info(args, number_of_variables):
        info.append(item)

    if number_of_variables == 1:
        s = ""
    else:
        s = "s"

    print(f"{number_of_variables} {args}{s} added successfully.")

def delete_item(args, info):
    list_items(args, info)
    print(f"Enter the {args}'s ID to delete:")
    id_to_delete = loop_positive_integer("ID to delete: ")

    for item in info:
        if item.show_student_id() == id_to_delete:
            info.remove(item)
            print(f"{args.capitalize()} with ID {id_to_delete} deleted successfully.")
            return

    print(f"Error: No {args} found with ID {id_to_delete}.")
    list_items(args, info)

def input_info(args, num):
    items = []
    if not num:
        print(f"Please input {args}(s) you want first.")
    else:
        for _ in range(num):
            item = {}
            print(f"Enter {args}'s ID: ")
            
            while True:
                item["id"] = loop_positive_integer("ID: ")
                item["name"] = input(f"Enter {args}'s name: ")
                
                if args == "student":
                    while True:
                        try:
                            dob = input(f"Enter {args} Date of Birth separate by '-' (YYYY-MM-DD): ")
                            dob_datetime = datetime.strptime(dob, "%Y-%m-%d")
                            item["dob"] = dob_datetime
                            break
                        except ValueError:
                            print("Error: Invalid date format. Please enter a valid date separate by '-' (YYYY-MM-DD).")
                else:
                    item["credit"] = loop_positive_integer(f"Please enter the number of {args}'s credit: ")

                if args == "student":
                    items.append(Student(**item))
                else:
                    items.append(Course(id=item["id"], name=item["name"], credit=item["credit"]))

                break
    return items

def input_mark(student_infos, course_infos, marks):
    if not student_infos or not course_infos:
        print("Please input students and courses first.")
        return

    list_items("student", student_infos)
    student_id = loop_positive_integer("Enter the student's ID for mark input: ")

    list_items("course", course_infos)
    course_id = loop_positive_integer("Enter the course's ID for mark input: ")

    for student in student_infos:
        if student.show_student_id() == student_id:
            for course in course_infos:
                if course.show_course_id() == course_id:
                    while True:
                        try:
                            mark_value = float(input(f"Enter the mark for {student.show_student_name()} in {course.show_course_name()}: "))
                            marks.append(Mark(student_id, course_id, mark_value))
                            print("Mark added successfully.")
                            return
                        except ValueError:
                            print("Error: Invalid mark. Please enter a valid number.")

    print(f"Error: No student or course found with ID {student_id} or {course_id}.")

def list_items(args, info):
    print(f"List of {args}: ")
    print("-" * 50)
    if args == "student":
        for item in info:
            print(f"ID: {item.show_student_id()}")
            print(f"Name: {item.show_student_name()}")
            print(f"Date of Birth: {item.show_dob().strftime('%Y-%m-%d')}")
            print("-" * 50)
    elif args == "course":
        for item in info:
            print(f"ID: {item.show_course_id()}")
            print(f"Name: {item.show_course_name()}")
            print(f"Credit: {item.show_credit()}")
            print("-" * 50)

def list_marks(marks, student_infos, course_infos):
    if not marks:
        print("No marks available.")
        return

    print("List of Marks:")
    for mark in marks:
        student_name = next((student.show_student_name() for student in student_infos if student.show_student_id() == mark.show_mark_student_id()), "Unknown Student")
        course_name = next((course.show_course_name() for course in course_infos if course.show_course_id() == mark.show_mark_course_id()), "Unknown Course")
        print(f"Student: {student_name}, Course: {course_name}, Mark: {mark.show_mark()}")

def main():
    student_array = StudentArray()
    course_array = CourseArray()
    marks = []

    while True:
        try:
            print("""
            0. Exit
            1. Input student(s).
            2. Input course(s).
            3. Delete specific student.
            4. Delete specific course.
            5. Input info of students.
            6. Input info of courses.
            7. Input marks.
            8. List students.
            9. List courses.
            10. List marks.
            """)

            option = int(input("Your choice: "))
            if option == 0:
                print("Exiting...")
                break

            elif option == 1:
                add_items(Student, "student", student_array.show_student_info())

            elif option == 2:
                add_items(Course, "course", course_array.show_course_info())

            elif option == 3:
                delete_item("student", student_array.show_student_info())

            elif option == 4:
                delete_item("course", course_array.show_course_info())

            elif option == 5:
                input_info("student", len(student_array.show_student_info()))

            elif option == 6:
                input_info("course", len(course_array.show_course_info()))

            elif option == 7:
                input_mark(student_array.show_student_info(), course_array.show_course_info(), marks)

            elif option == 8:
                list_items("student", student_array.show_student_info())

            elif option == 9:
                list_items("course", course_array.show_course_info())

            elif option == 10:
                list_marks(marks, student_array.show_student_info(), course_array.show_course_info())

            else:
                print("Invalid input. Please try again!")

        except ValueError:
            print("Error: Invalid input format.")

if _name_ == "_main_":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)