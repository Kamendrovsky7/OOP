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

    def __str__(self):
        avg_grade = self.average_grade_homework
        return f'Имя : {self.name} \nФамилия : {self.surname}\n' \
        f'Средняя оценка за домашние задания : {avg_grade()}\n' \
        f'Курсы в процессе изучения : {self.courses_in_progress}\n' \
        f'Завершеные курсы : {self.finished_courses}'

    def average_grade_homework(self):
        overall_grades = 0
        counter_grades = 0
        for course_grades in self.grades.values():
            overall_grades += sum(course_grades)
            counter_grades += len(course_grades)
            average_grade = overall_grades / counter_grades 
        if average_grade > 0:
            return average_grade
        else:
            return 0   
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя : {self.name} \nФамилия : {self.surname}'
        

class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        avg_grade = self.average_grade_lection
        return f'Имя : {self.name} \nФамилия : {self.surname} \nСредняя оценка за лекции : {avg_grade()}'
    
    def average_grade_lection(self):
        overall_grades = 0
        counter_grades = 0
        for course_grades in self.grades.values():
            overall_grades += sum(course_grades)
            counter_grades += len(course_grades)
            average_grade = overall_grades / counter_grades 
        if average_grade > 0:
            return average_grade
        else:
            return 0

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return super().__str__()
 
some_student = Student('Luke', 'Skywalker', 'Male')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']
 
any_lecturer = Lecturer('Obi-Van', 'Kenobi')
any_lecturer.courses_attached += ['Git', 'Python', 'Java']

some_reviewer = Reviewer ('Magister', 'Yoda')
some_reviewer.courses_attached += ['Python', 'Git']
 
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)

some_student.give_grades(any_lecturer, 'Git', 9.9)
some_student.give_grades(any_lecturer, 'Python', 9.9)
some_student.give_grades(any_lecturer, 'Python', 9.9)

print(some_student.grades)
print(any_lecturer.grades)

print(some_reviewer)
print(any_lecturer)
print(some_student)