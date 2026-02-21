class Student:
    def __init__(self, name, usn, marks):
        self.name = name
        self.usn = usn
        self.marks = marks  # dictionary {subject: mark}

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"


class ReportGenerator:
    def generate_report(self, student):
        print("\n===== STUDENT REPORT =====")
        print(f"Name : {student.name}")
        print(f"USN  : {student.usn}")

        print("\nMarks:")
        for subject, mark in student.marks.items():
            print(f"{subject} : {mark}")

        print("\nTotal   :", student.calculate_total())
        print("Average :", round(student.calculate_average(), 2))
        print("Grade   :", student.calculate_grade())
        print("==========================")
# Input section
name = input("Enter student name: ")
usn = input("Enter USN: ")

marks = {}
subjects = int(input("Enter number of subjects: "))

for i in range(subjects):
    sub = input("Enter subject name: ")
    mark = int(input(f"Enter marks for {sub}: "))
    marks[sub] = mark

# Object creation
student1 = Student(name, usn, marks)

# Generate report
report = ReportGenerator()
report.generate_report(student1)

