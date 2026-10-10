"""Make a Student class with a name, marks, and a method to give a grade."""


class Student:
    def __init__(self, name, marks, subject):
        self.name = name
        self.marks = marks
        self.subject = subject

    def grade(self):
        if self.marks >= 80:
            return "First grade"
        elif self.marks >= 40:
            return "Second grade"
        elif self.marks >= 20:
            return "Last grade"
        else:
            return "NG"


name = input("Enter the student's name: ")
marks = float(input("Enter the marks obtained: "))
subject = input("Enter the subject: ")

student = Student(name, marks, subject)
print(f"{student.name}: {student.grade()} in {student.subject}")
