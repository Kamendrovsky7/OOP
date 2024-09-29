class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def give_grades(self, lecturer, course, grade):
        if 1 <= grade <= 10:
            if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Можно выставить оценку только по десятибальной шкале'
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    grades = {}
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
some_student = Student('David', 'Beckham', 'Male')
some_student.courses_in_progress += ['Python', 'Git', 'Java']
 
any_lecturer = Lecturer('Obi','Van')
any_lecturer.courses_attached += ['Git', 'Python', 'Java']

some_reviewer = Reviewer ('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']
 
some_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)

some_student.give_grades(any_lecturer, 'Git', 9)
some_student.give_grades(any_lecturer, 'Java', 0)
some_student.give_grades(any_lecturer, 'Python', 10)

print(some_student.grades)
print(any_lecturer.grades)
print(some_student.name, some_student.surname)