import math

def input_student_info(mms):
    """Prompts user for student information and adds to the system."""
    try:
        num = int(input("Number of students to add: "))
    except ValueError:
        print("Invalid number.")
        return

    for _ in range(num):
        sid = input("Student ID: ")

        if mms.get_student(sid):
            print("Student ID already exists. Skipping.")
            continue

        name = input("Student name: ")
        dob = input("Student DoB (YYYY-MM-DD): ")

        mms.students.append(mms.domains.Student(sid, name, dob))
        print(f"Student {name} added.")

def input_course_info(mms):
    """Prompts user for course information and adds to the system."""
    try:
        num = int(input("Number of courses to add: "))
    except ValueError:
        print("Invalid number.")
        return

    for _ in range(num):
        cid = input("Course ID: ")

        if mms.get_course(cid):
            print("Course ID already exists. Skipping.")
            continue

        name = input("Course name: ")
        
        try:
            credit = int(input("Credit: "))
        except ValueError:
            print("Invalid credit value. Credit must be a whole number. Skipping course.")
            continue

        mms.courses.append(mms.domains.Course(cid, name, credit))
        print(f"Course {name} added.")

def input_marks(mms):
    """Prompts user for marks and assigns them to a student in a course."""
    print("\n--- Input Marks ---")
    cid = input("Enter course ID: ")

    course = mms.get_course(cid)
    if not course:
        print("Course not found.")
        return

    sid = input("Enter student ID: ")
    student = mms.get_student(sid)
    if not student:
        print("Student not found.")
        return

    try:
        mark = float(input("Enter mark (0–20): "))
        if not (0 <= mark <= 20):
            print("Mark must be between 0–20.")
            return
        floor_value = math.floor(mark)
        print(f"Original mark: {mark}, floored mark: {floor_value}")
    except ValueError:
        print("Invalid mark.")
        return

    course.assign_mark(sid, mark)
    print(f"Assigned mark {mark} to {student.name} for {course.name}.")