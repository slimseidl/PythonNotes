class Course:
    def __init__(self, number, title):
        self.number = number
        self.title=title

    def print_info(self):
        print(f'Course Information:')
        print(f'   Course Number: {self.number}')
        print(f'   Course Title: {self.title}')


class OfferedCourse(Course):
    def __init__(self, number, title, instructor_name, term, class_time):
        # Below calls the course class attributes so dont have to rewrite them
        Course.__init__(self, number,title)
        self.instructor_name = instructor_name
        self.term = term
        self.class_time = class_time

if __name__ == "__main__":
    course_number = input("Enter Course Number:\n")
    course_title = input("Enter Course Title:\n")

    o_course_number =  input("Enter another course number:\n")
    o_course_title =  input("Enter course title:\n")
    instructor_name = input("Enter Instructor Name:\n")
    term = input("Term:\n")
    class_time = input("Class Time:\n")
    
    my_course = Course(course_number, course_title)
    my_course.print_info()
    
    my_offered_course = OfferedCourse(o_course_number, o_course_title, instructor_name, term, class_time)
    my_offered_course.print_info()

    print('   Instructor Name:', my_offered_course.instructor_name)
    print('   Term:', my_offered_course.term)
    print('   Class Time:', my_offered_course.class_time)