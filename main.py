import numpy as np
import domains
import input
import output

class MarkManagementSystem:
    """Manages students, courses, marks, and calculations."""
    def __init__(self):
        self.domains = domains
        
        self.students = [
            self.domains.Student('001', 'A', '2001-01-01'),
            self.domains.Student('002', 'B', '2002-02-02'),
            self.domains.Student('003', 'C', '2003-03-03'),
            self.domains.Student('004', 'D', '2004-04-04'),
            self.domains.Student('005', 'E', '2005-05-05'),
        ]

        self.courses = [
            self.domains.Course('01', 'Math', 4),  
            self.domains.Course('02', 'Physics', 3),
            self.domains.Course('03', 'Chemistry', 3),
            self.domains.Course('04', 'Biology', 3),
            self.domains.Course('05', 'Geography2', 3),
        ]

    def get_student(self, sid):
        return next((s for s in self.students if s.id == sid), None)

    def get_course(self, cid):
        return next((c for c in self.courses if c.id == cid), None)
        
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
        """Calculates the GPA for all students and sorts the list in descending order."""
        if not self.students:
            print("No students registered to sort.")
            return

        student_gpas = []
        original_print = print
        print = lambda *a, **k: None 
        
        for student in self.students:
            gpa = self.calculate_gpa(student.id)
            sort_gpa = gpa if gpa is not None else 0.0
            student_gpas.append((student, sort_gpa))
            
        print = original_print 

        student_gpas.sort(key=lambda item: item[1], reverse=True)
        self.students = [item[0] for item in student_gpas]

        print("\nStudent List sorted.")
        output.list_students(self.students)


    def main_menu(self):
        while True:
            print("\n--- Mark Management System ---")
            print("1. Input student info")
            print("2. List students")
            print("3. List courses")
            print("4. Input course info")
            print("5. Input marks")
            print("6. Calculate GPA/WAM for a student")
            print("7. Sort student list by GPA descending")
            print("0. Exit")

            choice = input("Enter choice: ").strip()

            if choice == '1':
                input.input_student_info(self) 
            elif choice == '2':
                output.list_students(self.students) 
            elif choice == '3':
                output.list_courses(self.courses) 
            elif choice == '4':
                input.input_course_info(self) 
            elif choice == '5':
                input.input_marks(self) 
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