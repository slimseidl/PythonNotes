class Student:
    def __init__(self, first, last, gpa):
        self.first = first # first name
        self.last = last   # last name
        self.gpa = gpa     # grade point average

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last

class Course:
    def __init__(self):
        self.roster = []  # list of Student objects

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    def find_student_highest_gpa(self):
        top_student = self.roster[0]
        for student in self.roster:
            if student.get_gpa() > top_student.get_gpa():
                top_student = student
            else:
                continue
        return top_student


course = Course()
# Adding students from input
while True:
    stop = input("Press 1 to terminate or any other key to add a new student:\n")
    if stop == "1":
        break

    first = input("Enter Student First Name:\n")
    last = input("Enter Student Last Name:\n")
    gpa = float(input("Enter Student GPA:\n"))

# course.add_student(Student('Henry', 'Nguyen', 3.5))
# course.add_student(Student('Brenda', 'Stern', 2.0))
# course.add_student(Student('Lynda', 'Robison', 3.2))
# course.add_student(Student('Sonya', 'King', 3.9))
# comment

    # Calling the studnet class to add students
    course.add_student(Student(first,last,gpa))

student = course.find_student_highest_gpa()
print('Top student:', student.first, student.last, '( GPA:', student.gpa,')')