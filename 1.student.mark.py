students = [
    {'id': '001', 'name': 'A', 'DoB': '2001-01-01'},
    {'id': '002', 'name': 'B', 'DoB': '2002-02-02'},
    {'id': '003', 'name': 'C', 'DoB': '2003-03-03'},
    {'id': '004', 'name': 'D', 'DoB': '2004-04-04'},
    {'id': '005', 'name': 'E', 'DoB': '2005-05-05'},
]

courses = [
    {'id': '01', 'name': 'Math', 'marks': {}},
    {'id': '02', 'name': 'Physics', 'marks': {}},
    {'id': '03', 'name': 'Chemistry', 'marks': {}},
    {'id': '04', 'name': 'Biology', 'marks': {}},
    {'id': '05', 'name': 'Geography2', 'marks': {}},
]
def input_student_info():
    try:
        num_students = int(input("Number of students to add: "))
    except ValueError:
        print("Invalid ")
        return

    for _ in range(num_students):
        s_id = input("Student ID: ")
        s_name = input("Student name: ")
        s_dob = input("Student DoB (YYYY-MM-DD): ")

        student = {'id': s_id, 'name': s_name, 'DoB': s_dob}
        students.append(student)
        print(f"Student {s_name} added.")


def input_course_info():
    try:
        num_courses = int(input("Number of courses to add: "))
    except ValueError:
        print("Invalid")
        return

    for _ in range(num_courses):
        c_id = input("Course ID: ")
        c_name = input("Course name: ")

        course = {'id': c_id, 'name': c_name, 'marks': {}}
        courses.append(course)
        print(f"Course {c_name} added.")


def list_students():
    print("\nStudent List:")
    if not students:
        print("No students registered.")
        return

    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['DoB']}")


def list_courses():
    print("\nCourse List:")
    if not courses:
        print("No courses registered.")
        return

    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")
def input_marks():
    print("\n--- Input Marks ---")
    course_id = input("Enter course ID: ")
    course = next((c for c in courses if c["id"] == course_id), None)

    if not course:
        print("Course not found.")
        return
    student_id = input("Enter student ID: ")
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        print("Student not found.")
        return
    try:
        mark = float(input("Enter mark (0-20): "))
        if mark < 0 or mark > 20:
            print("Mark must be between 0-20.")
            return
    except ValueError:
        print("Invalid mark.")
        return
    course["marks"][student_id] = mark
    print(f"Mark {mark} assigned {student['name']} in {course['name']}.")
def main_menu():
    while True:
        print("\n===== Mark Management System =====")
        print("1. Input student info")
        print("2. List students")
        print("3. List courses")
        print("4. Input course info")
        print("5. Input marks")
        print("0. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            input_student_info()
        elif choice == '2':
            list_students()
        elif choice == '3':
            list_courses()
        elif choice == '4':
            input_course_info()
        elif choice == '5':
            input_marks()
        elif choice == '0':
            print("Exiting")
            break
        else:
            print("Invalid")
if __name__ == "__main__":
    main_menu()
