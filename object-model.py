class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade
    
    def get_info(self):
        return f"{self.name} is in grade {self.grade}."

class Subject:
    def __init__(self, name: str):
        self.name = name
        self.grades = {}  

    def add_grade(self, student: Student, grade: int):
        if student not in self.grades:
            self.grades[student] = []
        self.grades[student].append(grade)

class Diary:
    def __init__(self, student: Student):
        self.student = student
        self.subjects = []

    def add_subject(self, subject: Subject):
        self.subjects.append(subject)

    def show_grades(self):
        print(f"Grades for {self.student.name}:")
        for subject in self.subjects:
            if self.student in subject.grades:
                print(f"{subject.name}: {subject.grades[self.student]}")
                

student1 = Student("Alice", 9)
student2 = Student("Bob", 9)

math = Subject("Math")
science = Subject("Science")

diary1 = Diary(student1)
diary1.add_subject(math)
diary1.add_subject(science)

diary2 = Diary(student2)
diary2.add_subject(math)
diary2.add_subject(science)


math.add_grade(student1, 5)
math.add_grade(student1, 4)

science.add_grade(student1, 3)
science.add_grade(student1, 4)

math.add_grade(student2, 3)
math.add_grade(student2, 5)


diary1.show_grades()
diary2.show_grades()