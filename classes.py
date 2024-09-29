class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # создание функции оценки студентами лекторов

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
    
    # подсчет средней оценки за домашнее задания

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

    def average_grade_homework_in_course(student, grade):
        overall_grades = 0
        counter_grades = 0
        for student in students:
            if self.course in student.grades:
                overall_grades += sum(student.grades[course])
                counter_grades += len(student.grades[course])
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
        
# создание класса на основе родительского Mentor
class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        avg_grade = self.average_grade_lection
        return f'Имя : {self.name} \nФамилия : {self.surname} \nСредняя оценка за лекции : {avg_grade()}'
    
    #подсчет средней оценки за лекции

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

#создание класса на основе родительского Mentor
class Reviewer(Mentor):
    # оценка студентов по курсу
    def rate_hw(self, student, course, grade):
        if 1 <= grade <= 10:
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

# Вывод оценок студентов за курс и оценок лекторов за лекции

print(some_student.grades)
print(any_lecturer.grades)

# Вывод магического метода __str__

print(some_reviewer)
print(any_lecturer)
print(some_student)

# Полевое задание

first_student = Student('Han', 'Solo', 'male')
second_student = Student('Leya', 'Organa', 'female')
first_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Python']

first_lecturer = Lecturer('George', 'Lukas')
second_lecturer = Lecturer('Carrie', 'Fisher')
first_lecturer.courses_attached += ['Python'] 
second_lecturer.courses_attached += ['Python']

first_reviewer = Reviewer('Alan', 'Moore')
second_reviewer = Reviewer('Donna', 'Tarth')

# оценка студентов

first_reviewer.rate_hw(first_student, "Python", 10)
first_reviewer.rate_hw(second_student, "Python", 9)
second_reviewer.rate_hw(first_student, "Pyhton", 7)
second_reviewer.rate_hw(second_student, "Python", 8)

# оценка разными студентами разных лекторов по курсу

first_student.give_grades(first_lecturer,'Python',10)
first_student.give_grades(second_lecturer,'Python',10)

second_student.give_grades(first_lecturer,'Python',8)
second_student.give_grades(second_lecturer,'Python',6)

# функция на подсчет средней оценки по выбранному курсу
def average_grade_homework_in_course(student, grade):
        overall_grades = 0
        counter_grades = 0
        courses = 0
        for student in students:
            if courses in student.grades:
                overall_grades += sum(student.grades[courses])
                counter_grades += len(student.grades[courses])
                average_grade = overall_grades / counter_grades 
        return overall_grades / counter_grades if counter_grades > 0 else 0

def average_grade_lection_in_course(lecturer, grade):
        overall_grades = 0
        counter_grades = 0
        courses = None
        for lecturer in lecturers:
            if courses in lecturer.grades:
                overall_grades += sum(lecturer.grades[courses])
                counter_grades += len(lecturer.grades[courses])
                average_grade = overall_grades / counter_grades 
        return overall_grades / counter_grades if counter_grades > 0 else 0

lecturers = [first_lecturer,second_lecturer]
students = [first_student,second_student]

print(f'Средняя оценка по всем студентам в рамках курса : {average_grade_homework_in_course(students, "Python")}')

print(f'Средняя оценка по всем лекторам в рамках курса : {average_grade_lection_in_course(lecturers, "Python")}')