import datetime

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def display_info(self):
        print(f"Name: {self.name}, Date of Birth: {self.dob}")


class Course:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.id] = student

    def list_students(self):
        print(f"Course: {self.name}")
        if self.students:
            for student_id, student in self.students.items():
                student.list_marks()
                print()
        else:
            print("No students enrolled.")

    def display_info(self):
        print(f"Course Name: {self.name}")


class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(name, dob)
        self.id = id
        self.marks = {}

    def input_marks(self, course, mark):
        self.marks[course] = mark

    def list_marks(self):
        super().display_info()
        if self.marks:
            print("Marks:")
            for course, mark in self.marks.items():
                print(f"  {course}: {mark}")
        else:
            print("No marks available.")


def create_student(existing_ids):
    while True:
        id = input("Enter student ID: ")
        if id in existing_ids:
            print("Caution: The entered student ID already exists. Please check the document again.")
        else:
            existing_ids.add(id)
            break

    name = input("Enter student name: ")
    
    # Date of birth input with validation
    while True:
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        try:
            year, month, day = map(int, dob.split('-'))
            datetime.datetime(year, month, day)
            if month > 12 or day > 31 or (day > 30 and month in [4, 6, 9, 11]) or (month == 2 and day > 29):
                raise ValueError("Invalid day or month.")
            break
        except ValueError:
            print("Invalid date format or out of range. Please enter a valid date.")

    return Student(id, name, dob)


def create_course():
    while True:
        num_courses = input("Enter the number of courses: ")
        if num_courses.isdigit():
            break
        else:
            print("Caution: Number of courses needs to be a number. Please try again.")
    name = input("Enter course name: ")
    return Course(name)


def main():
    courses = []
    while True:
        try:
            num_courses = int(input("Enter the number of courses: "))
            break
        except ValueError:
            print("Caution: Number of courses needs to be a number. Please try again.")

    for _ in range(num_courses):
        course = create_course()
        courses.append(course)

    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            break
        except ValueError:
            print("Caution: Number of students needs to be a number. Please try again.")

    students = []
    existing_ids = set()  # Set to store existing student IDs
    for _ in range(num_students):
        student = create_student(existing_ids)
        students.append(student)

    print("\nEnrolling students in courses:")
    for course in courses:
        print(f"\nFor course '{course.name}':")
        for student in students:
            response = input(f"Do you want to enroll {student.name} (ID: {student.id}) in this course? (y/n): ")
            if response.lower() == 'y':
                course.add_student(student)
                while True:
                    try:
                        mark = int(input(f"Enter mark for {student.name} in {course.name}: "))
                        if 0 <= mark <= 20:
                            student.input_marks(course.name, mark)
                            break
                        else:
                            print("Invalid mark. Mark must be between 0 and 20.")
                    except ValueError:
                        print("Invalid mark input. Mark must be a number.")

    print("\nListing students in courses:")
    for course in courses:
        course.list_students()
        
if __name__ == "__main__":
    main()
