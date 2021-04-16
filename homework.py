class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        ans = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: ' \
              f'{sum(map(sum, self.grades.values())) / len(self.grades.values())}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} ' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'

        return ans

    def rate_hw_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            lecturer.grades.append(grade)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        ans = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {int(sum(self.grades)) / len(self.grades)}'
        return ans

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            self_avg = int(sum(self.grades)) / len(self.grades)
            other_avg = int(sum(other.grades)) / len(other.grades)
            return self_avg < other_avg


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if type(grade) != int or 10 < grade or grade < 0:
            return print(f'Оценка {grade} не корректна')
        else:
            if isinstance(self, Reviewer):
                if isinstance(student, Student) and course in self.courses_attached \
                        and course in student.courses_in_progress:
                    if course in student.grades:
                        student.grades[course] += [grade]
                    else:
                        student.grades[course] = [grade]

    def __str__(self):
        if isinstance(self, Reviewer):
            ans = f'Имя: {self.name}\nФамилия: {self.surname}'
            return ans


first_lecturer = Lecturer('Alexey', 'Navalny')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']
second_lecturer = Lecturer('Vladimir', 'Putin')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

first_student = Student('Yagami', 'Light', 'Male')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
second_student = Student('Levi', 'Akkerman', 'Male')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']

cool_reviewer = Reviewer('Ivan', 'Ivanovich')
best_reviewer = Reviewer('Ecio', 'Auditore')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
best_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(first_student, 'Python', 10)
cool_reviewer.rate_hw(first_student, 'Python', 7)
cool_reviewer.rate_hw(second_student, 'Python', 8)
cool_reviewer.rate_hw(second_student, 'Python', 10)
cool_reviewer.rate_hw(first_student, 'Git', 10)
cool_reviewer.rate_hw(second_student, 'Git', 5)

first_student.rate_hw_lector(first_lecturer, 'Git', 10)
first_student.rate_hw_lector(first_lecturer, 'Python', 5)
first_student.rate_hw_lector(second_lecturer, 'Git', 10)
second_student.rate_hw_lector(second_lecturer, 'Python', 10)
students = [first_student, second_student]
lecturers = [first_lecturer, second_lecturer]


def avg_hw_stds(std_list, course):
    grades = []
    for i in std_list:
        if course in i.courses_in_progress:
            grades.append((sum(i.grades[course])))
    a = sum(grades) / len(std_list)
    return a


def avg_hw_lecturers(lecturers_list, course):
    grades = []
    for i in lecturers_list:
        if course in i.courses_attached:
            grades.append((sum(i.grades)))
            a = sum(grades) / len(lecturers_list)
            return a
