def list_students(students):
    """Prints the list of all registered students."""
    print("\nStudent List:")
    if not students:
        print("No students registered.")
        return
    for s in students:
        print(s)

def list_courses(courses):
    """Prints the list of all registered courses and their marks."""
    print("\nCourse List:")
    if not courses:
        print("No courses registered.")
        return

    for c in courses:
        print(c)
        if c.marks:
            print("  Marks:")
            for sid, mark in c.marks.items():
                print(f"    Student {sid}: {mark}")
        else:
            print("  No marks assigned yet.")