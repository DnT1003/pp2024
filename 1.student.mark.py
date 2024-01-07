def input_number_of_students():
    while True:
        try:
            num_students = int(input("Enter number of students in class: "))
            if num_students > 0:
                return num_students
            else:
                print("Please enter a valid natural number (greater than zero).")
        except ValueError:
            print("Invalid input. Please enter a valid natural number.")

def input_student_information():
    students = []
    num_students = input_number_of_students()
    for i in range(num_students):
        s_id = input(f"Enter ID for student {i + 1}: ")
        s_name = input(f"Enter name for student {i + 1}: ")
        s_dob = input(f"Enter DoB for student {i + 1} (dd-mm-yyyy): ")
        while not (s_id and s_name and s_dob):
            print("You haven't input anything. Please provide all information.")
            s_id = input(f"Enter ID for student {i + 1}: ")
            s_name = input(f"Enter name for student {i + 1}: ")
            s_dob = input(f"Enter DoB for student {i + 1} (dd-mm-yyyy): ")

        s_info = {"id": s_id, "name": s_name, "DoB": s_dob}
        students.append(s_info)
    return students

def input_number_of_courses():
    while True:
        try:
            num_courses = int(input("Enter number of courses: "))
            if num_courses > 0:
                return num_courses
            else:
                print("Please enter a valid natural number (greater than zero).")
        except ValueError:
            print("Invalid input. Please enter a valid natural number.")
    
def input_course_information():
    courses = []
    num_courses = input_number_of_courses()
    for i in range(num_courses):
        c_id = input(f"Enter ID for course {i + 1}: ")
        c_name = input(f"Enter name for course {i + 1}: ")
        while not (c_id and c_name):
            print("You haven't input anything. Please provide all information.")
            c_id = input(f"Enter ID for course {i + 1}: ")
            c_name = input(f"Enter name for course {i + 1}: ")
        
        c_info = {"id": c_id, "name": c_name}
        courses.append(c_info)
    return courses

def select_course(courses):
    print("Available courses:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course['name']}")
    choice = int(input("Select a course (enter its number): ")) - 1
    return courses[choice]

def input_marks(students, selected_course):
    print(f"Enter marks for students in {selected_course['name']} course:")
    for i, student in enumerate(students, 1):
        mark = float(input(f"Enter mark for {student['name']} in {selected_course['name']}: "))
        student[selected_course['id']] = mark

def display_student_information(s_info):
    print("\nStudent Information:")
    for student in s_info:
        print(student)

def display_student_marks(selected_course, s_info):
    print(f"\nMarks for {selected_course['name']} course:")
    for student in s_info:
        if selected_course['id'] in student:
            print(f"{student['name']}: {student[selected_course['id']]}")

students = input_student_information()
courses = input_course_information()
selected_course = select_course(courses)
input_marks(students, selected_course)
display_student_information(students)
display_student_marks(selected_course, students)
