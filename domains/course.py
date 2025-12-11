class Course:
    """Represents a course, holding its details and student marks."""
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