class Courses:
    def __init__(self):
        self.courses = {}

    def add_student(self, course, student):
        if course not in self.courses:
            self.courses[course] = []
        self.courses[course].append(student)

    def __repr__(self):
        course_repr = []
        for course, students in self.courses.items():
            course_repr.append(f"{course}: {len(students)}")
            for student in students:
                course_repr.append(f"-- {student}")
        return '\n'.join(course_repr)


uni_course = Courses()

while True:
    command_line = input()
    if command_line == "end":
        break
    else:
        course_name, student_name = command_line.split(" : ")
        uni_course.add_student(course_name, student_name)

print(uni_course.__repr__())
