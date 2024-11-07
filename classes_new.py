from operator import lt, eq

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def give_grades(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
   
    def av_grade(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_grade = round(sum_rating / len_rating, 2)
        return average_grade

    def av_grade_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_grade = round(sum_rating / len_rating, 2)
        return average_grade               

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'\
        f'Средняя оценка за домашние задания: {self.av_grade()}\n'\
        f'Курсы в процессе изучения: {(self.courses_in_progress)}\n'\
        f'Завершенные курсы: {(self.finished_courses)}'
        
        

    def __lt__(self, other):
        return self.av_grade() < other.av_grade()

    def __eq__(self,other):
        return self.av_grade() == other.av_grade()





class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def av_grade(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_grade = round(sum_rating / len_rating, 2)
        return average_grade

    def av_grade_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_grade = round(sum_rating / len_rating, 2)
        return average_grade   

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'\
        f'Средняя оценка за лекции: {self.av_grade()}'
        
    
    def __lt__(self, other):
        return self.av_grade() < other.av_grade()

    def __eq__(self,other):
        return self.av_grade() == other.av_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


# Студенты
student_1 = Student('Han', 'Solo', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Введение в програмирование"]

student_2 = Student('Leya', 'Organa', 'female')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Введение в програмирование"]

# Лекторы
lecturer_1 = Lecturer('George', 'Lucas')
lecturer_1.courses_attached += ['Python']
 
lecturer_2 = Lecturer('Carrie', 'Fisher')
lecturer_2.courses_attached += ['Python']

# Проверяющие
reviewer_1 = Reviewer('Alan', 'Moore')
reviewer_1.courses_attached += ['Python']
 
reviewer_2 = Reviewer('Donna', 'Tarth')
reviewer_2.courses_attached += ['Python']

# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 9)

# Оценки лекторам
student_1.give_grades(lecturer_1, 'Python', 10)
student_1.give_grades(lecturer_1, 'Python', 10)
student_1.give_grades(lecturer_1, 'Python', 10)

student_2.give_grades(lecturer_2, 'Python', 10)
student_2.give_grades(lecturer_2, 'Python', 10)
student_2.give_grades(lecturer_2, 'Python', 10)

students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]
reviewers = [reviewer_1, reviewer_2]

def average_grade_for_course(course, students):
    sum_rating = 0
    quantity_rating = 0
    for stud in students:
        for course in stud.grades:
            stud_sum_rating = stud.av_grade_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_grade = round(sum_rating / quantity_rating, 2)
    return average_grade

#вывод магического __str__

print(student_1,'\n')
print(student_2,'\n')
print(lecturer_1,'\n')
print(lecturer_2,'\n')

#Вывод магического __lt__ ,__eq__

if lecturer_1 < lecturer_2: 
    print (f'{lecturer_1.name} {lecturer_1.surname} имеет более низкую среднюю оценку, чем {lecturer_2.name} {lecturer_2.surname}','\n')
elif lecturer_1 == lecturer_2:
    print (f'{lecturer_1.name} {lecturer_1.surname} имеют равные оценки {lecturer_2.name} {lecturer_2.surname}','\n')
else:
    print (f'{lecturer_1.name} {lecturer_1.surname} имеет более высокую среднюю оценку, чем {lecturer_2.name} {lecturer_2.surname}','\n')

if student_1 < student_2: 
    print (f'{student_1.name} {student_1.surname} имеет более низкую среднюю оценку, чем {student_2.name} {student_2.surname}','\n')
elif student_1 == student_2:
    print (f'{lstudent_1.name} {student_1.surname} имеют равные оценки {student_2.name} {student_2.surname}','\n')
else:
    print (f'{student_1.name} {student_1.surname} имеет более высокую среднюю оценку, чем {student_2.name} {student_2.surname}','\n')


#Вывод средних оценок по конкретным группам

print(f'Средняя оценка по всем студентам в рамках курса : {average_grade_for_course('Python', students)}')
print(f'Средняя оценка по всем лекторам в рамках курса : {average_grade_for_course('Python', lecturers)}')