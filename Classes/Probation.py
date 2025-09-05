class Student:
    def __init__(self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa 

    def get_gpa(self):
        return self.gpa
    
    def get_last(self):
        return self.last 
    

class Course:
    def __init__(self):
        self.roster = [] 
        # list of student objects 

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)
    
    def count_probation(self):
        probation_students = []
        for student in self.roster:
            if student.get_gpa() < 2.0:
                probation_students.append(student)
            else:
                continue
        return len(probation_students)
    

course = Course()
# Below instantiates the student class within the course class and allows the count_probation method to be called! 
course.add_student(Student('Henry', 'Cabot', 3.2))
course.add_student(Student('Brenda', 'Stern', 1.1))
course.add_student(Student('Lynda', 'Robison', 2.4))
course.add_student(Student('Jane', 'Flynn', 1.8))

probation_count = course.count_probation()
print(f'Probation Count: {probation_count}')
