class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
        self.marks = {} 

    def assign_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class MarkManagementSystem:
    def __init__(self):
        self.students = [
            Student('001', 'A', '2001-01-01'),
            Student('002', 'B', '2002-02-02'),
            Student('003', 'C', '2003-03-03'),
            Student('004', 'D', '2004-04-04'),
            Student('005', 'E', '2005-05-05'),
        ]

        self.courses = [
            Course('01', 'Math'),
            Course('02', 'Physics'),
            Course('03', 'Chemistry'),
            Course('04', 'Biology'),
            Course('05', 'Geography2'),
        ]

    def get_student(self, sid):
        return next((s for s in self.students if s.id == sid), None)

    def get_course(self, cid):
        return next((c for c in self.courses if c.id == cid), None)
    def input_student_info(self):
        try:
            num = int(input("Number of students to add: "))
        except ValueError:
            print("Invalid number.")
            return

        for _ in range(num):
            sid = input("Student ID: ")

            if self.get_student(sid):
                print("Student ID already exists. Skipping.")
                continue

            name = input("Student name: ")
            dob = input("Student DoB (YYYY-MM-DD): ")

            self.students.append(Student(sid, name, dob))
            print(f"Student {name} added.")

    def list_students(self):
        print("\nStudent List:")
        if not self.students:
            print("No students registered.")
            return
        for s in self.students:
            print(s)
    def input_course_info(self):
        try:
            num = int(input("Number of courses to add: "))
        except ValueError:
            print("Invalid number.")
            return

        for _ in range(num):
            cid = input("Course ID: ")

            if self.get_course(cid):
                print("Course ID already exists. Skipping.")
                continue

            name = input("Course name: ")

            self.courses.append(Course(cid, name))
            print(f"Course {name} added.")

    def list_courses(self):
        print("\nCourse List:")
        if not self.courses:
            print("No courses registered.")
            return

        for c in self.courses:
            print(c)
            if c.marks:
                print("  Marks:")
                for sid, mark in c.marks.items():
                    print(f"    Student {sid}: {mark}")
            else:
                print("  No marks assigned yet.")

    def input_marks(self):
        print("\n--- Input Marks ---")
        cid = input("Enter course ID: ")

        course = self.get_course(cid)
        if not course:
            print("Course not found.")
            return

        sid = input("Enter student ID: ")
        student = self.get_student(sid)
        if not student:
            print("Student not found.")
            return

        try:
            mark = float(input("Enter mark (0–20): "))
            if not (0 <= mark <= 20):
                print("Mark must be between 0–20.")
                return
        except ValueError:
            print("Invalid mark.")
            return

        course.assign_mark(sid, mark)
        print(f"Assigned mark {mark} to {student.name} for {course.name}.")

    def main_menu(self):
        while True:
            print("\n===== Mark Management System (OOP Version) =====")
            print("1. Input student info")
            print("2. List students")
            print("3. List courses")
            print("4. Input course info")
            print("5. Input marks")
            print("0. Exit")

            choice = input("Enter choice: ").strip()

            if choice == '1':
                self.input_student_info()
            elif choice == '2':
                self.list_students()
            elif choice == '3':
                self.list_courses()
            elif choice == '4':
                self.input_course_info()
            elif choice == '5':
                self.input_marks()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    system = MarkManagementSystem()
    system.main_menu()
