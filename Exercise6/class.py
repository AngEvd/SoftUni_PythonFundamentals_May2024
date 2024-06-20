class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.students = []
        self.grades = []
        self.name = name

    def add_student(self, name: str, grade: float):
        if len(self.students) < 22:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0.0
        else:
            return float(f"{sum(self.grades) / len(self.grades):.2f}")

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"
