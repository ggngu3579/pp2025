import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, name, credit):
        try:
            self.id = course_id
            self.name = name
            self.credit = int(credit) 
        except ValueError:
             print(f"Warning: Credit for course {name} must be a number. Defaulting to 0.")
             self.credit = 0
             
        self.marks = {} 

    def assign_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Credit: {self.credit}"


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
            Course('01', 'Math', 4),  
            Course('02', 'Physics', 3),
            Course('03', 'Chemistry', 3),
            Course('04', 'Biology', 3),
            Course('05', 'Geography2', 3),
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
            
            try:
                credit = int(input("Credit: "))
            except ValueError:
                print("Invalid credit value. Credit must be a whole number. Skipping course.")
                continue

            self.courses.append(Course(cid, name, credit))
            print(f"Course {name} added.")

    def list_courses(self):
        print("\nCourse List:")
        if not self.courses:
            print("No courses registered.")
            return

        for c in self.courses:
            print(c)
            if c.marks:
                print("  Marks:")
                for sid, mark in c.marks.items():
                    print(f"    Student {sid}: {mark}")
            else:
                print("  No marks assigned yet.")

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
            floor_value = math.floor(mark)
            print(f"Original mark: {mark}, floored mark: {floor_value}")
        except ValueError:
            print("Invalid mark.")
            return

        course.assign_mark(sid, mark)
        print(f"Assigned mark {mark} to {student.name} for {course.name}.")
        
    def calculate_gpa(self, student_id):
        marks = []
        credits = []

        for course in self.courses:
            if student_id in course.marks:
                marks.append(course.marks[student_id])
                credits.append(course.credit)

        if not marks:
            print("No marks for this student.")
            return None

        marks_arr = np.array(marks)
        credits_arr = np.array(credits)

        weighted_sum = np.sum(marks_arr * credits_arr)
        total_credits = np.sum(credits_arr)
        
        if total_credits == 0:
            print("Total credit is 0, cannot calculate WAM/GPA.")
            return 0.0
            
        gpa = weighted_sum / total_credits

        print(f"\nWeighted Average Mark (WAM) for Student {student_id}")
        print(f"Marks: {marks_arr}")
        print(f"Credits: {credits_arr}")
        print(f"Weighted sum: {weighted_sum}")
        print(f"Total credits: {total_credits}")
        print(f"Average WAM (0-20 scale): {gpa:.2f}")

        return gpa
    
    def sort_students_by_gpa(self):
        if not self.students:
            print("No students registered to sort.")
            return
        student_gpas = []
        for student in self.students:
            gpa = self.calculate_gpa(student.id)
            sort_gpa = gpa if gpa is not None else 0.0
            student_gpas.append((student, sort_gpa))
        student_gpas.sort(key=lambda item: item[1], reverse=True)
        self.students = [item[0] for item in student_gpas]

        print("\nSorting student list")
        self.list_students()


    def main_menu(self):
        while True:
            print("\n--- Mark Management System ---")
            print("1. Input student info")
            print("2. List students")
            print("3. List courses")
            print("4. Input course info")
            print("5. Input marks")
            print("6. Calculate GPA/WAM for a student")
            print("7. Sort student list")
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
            elif choice == '6':
                sid = input("Enter student ID: ")
                self.calculate_gpa(sid)
            elif choice == '7':
                self.sort_students_by_gpa()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
    


if __name__ == "__main__":
    system = MarkManagementSystem()
    system.main_menu()