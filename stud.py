class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [rate]
            else:
                lecturer.grades[course] = [rate]
        else:
            return 'Ошибка'

    def __str__(self):
        output = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за домашние задания: {average_grade(self.grades)}\n' \
                 f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
                 f'Завершенные курсы: {self.finished_courses}'
        return output

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("NO")
            return
        elif average_grade(self.grades) < average_grade(other.grades):
            return f'Средняя оценка студента {other.name} больше средней оценки {self.name}'
        elif average_grade(self.grades) > average_grade(other.grades):
            return f'Средняя оценка студента {self.name} больше средней оценки {other.name}'
        elif average_grade(self.grades) == average_grade(other.grades):
            return f'Средние оценки студентов {self.name} и {other.name} равны'
        else:
            return average_grade(self.grades) < average_grade(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(average_grade(self.grades), 2)}'
        return output

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("NO")
            return
        elif average_grade(self.grades) < average_grade(other.grades):
            return f'Средняя оценка лектора {other.name} больше средней оценки {self.name}'
        elif average_grade(self.grades) > average_grade(other.grades):
            return f'Средняя оценка лектора {self.name} больше средней оценки {other.name}'
        elif average_grade(self.grades) == average_grade(other.grades):
            return f'Средние оценки лекторов {self.name} и {other.name} равны'
        else:
            return average_grade(self.grades) < average_grade(other.grades)

# Функция для подсчета средней оценки за домашки
def average_grade(listResults):
    allRatings = []
    if (len(listResults)):
        for grades in listResults.values():
            allRatings += grades
        return sum(map(lambda x: int(x), allRatings)) / len(allRatings)
    else:
        return 'Оценок нет'

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
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output

# функция для подсчета средней оценки за ДЗ по всем студентам в рамках конкретного курса
def average_course_grade(all_students, current_course):
    all_course_grades = []
    for current_student in all_students:
        if current_course in current_student.grades.keys():
            for every_grade in current_student.grades.get(current_course):
                all_course_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у студента: {current_student.name} {current_student.surname}')
    return f'Средний балл за ДЗ по всем студентам равен {sum(all_course_grades)/len(all_course_grades)}'

# Функция расчета среднего значения оценок лекторов:
def average_lecturers_grade(all_lecturers, current_course):
    all_lecturers_grades = []
    for current_lecturer in all_lecturers:
        if current_course in current_lecturer.grades.keys():
            for every_grade in current_lecturer.grades.get(current_course):
                all_lecturers_grades.append(every_grade)
        else:
            print(f'Курс {current_course} отсутствует у лектора: {current_lecturer.name} {current_lecturer.surname}')
    return f'Средний балл за лекции по курсу {current_course} равен {sum(all_lecturers_grades) / len(all_lecturers_grades)}'

    #     all_lecturers_grades += average_grade(current_lecturer.grades)
    # return all_lecturers_grades / len(all_lecturers)

# Создание экземпляра класса Студент:
student_1 = Student('Василий', 'Андронов', '100')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['JS']
student_1.finished_courses += ['Java']

student_2 = Student('Мария', 'Андронова', '18')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Git']

# Создание экземпляра класса Lecturer:
lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['JS']

lecturer_2 = Lecturer('Александр', 'Бардин')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Node']
lecturer_2.courses_attached += ['Git']

# Создание экземпляра класса Reviewer:
reviewer1 = Reviewer('Павел', 'Павлов')
reviewer1.courses_attached += ['Python', 'JS']

reviewer2 = Reviewer('Петр', 'Петров')
reviewer2.courses_attached += ['Git', 'Python']

# проверяющий проставляет оценки студенту:
reviewer1.rate_hw(student_1, 'Python', 5)
reviewer1.rate_hw(student_1, 'Python', 6)
reviewer1.rate_hw(student_1, 'JS', 10)
print(f'Проверка получения оценки student_1 от reviewer1')
print(f'Оценки (студент {student_1.name}) {student_1.grades}\n')

reviewer2.rate_hw(student_2, 'Python', 9)
reviewer2.rate_hw(student_2, 'Python', 8)
reviewer2.rate_hw(student_2, 'Git', 6)

# Студент проставляет оценки преподавателю:
student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'JS', 7)
print(f'Проверка получения оценки lecturer_1 от student_1')
print(f'Оценки (лектор {lecturer_1.name}) {lecturer_1.grades}\n')

student_2.rate_lecturer(lecturer_2, 'Python', 6)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Node', 8)

# ПРОВЕРКА average_course_grade(all_students, current_course)
print('Проверка расчета средней оценки за домашние задания по всем студентам по одному курсу')
student_list = [student_1, student_2]
print(average_course_grade(student_list, 'Python'), "\n")

# ПРОВЕРКА average_lecturers_grade(all_lecturers, current_course)
print('Проверка расчета средней оценки у лекторов')
lecturer_list = [lecturer_1, lecturer_2]
print(f'{average_lecturers_grade(lecturer_list, "Python")}\n')

# ПРОВЕРКА вывода инфо по студенту, лектору (функция str)
print('Проверка вывода инфо по студенту')
print(student_1,"\n")
print('Проверка вывода инфо по лектору')
print(lecturer_1.__str__(),"\n")
print('Проверка вывода инфо по проверяющему')
print(reviewer1.__str__(),"\n")

# ПРОВЕРКА сравнение средних оценок между студентами
print('Проверка сравнения средних оценок между студентами')
print(student_1 < student_2)
print(lecturer_1 < lecturer_2)