class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.lecturergrades = {}     
    def __aver_lect(self,lecturergrades):
        return round(sum(lecturergrades.values())/len(lecturergrades),1)
    def __str__(self,lecturergrades):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__aver_lect(lecturergrades)}"
    
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
        return f"Имя:{self.name}\nФамилия:{self.surname}"
    
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_courses(self, course_name):
        self.finished_course.append(course_name)
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Mentor) and course in self.courses_attached and course in self.courses_in_progress and 0 <= grade <= 10:
            if course in self.finished_courses:
                lecturer.lecturergrades[course] += [grade]
            else:
                lecturer.lecturergrades[course] = [grade]
        else:
            return 'Ошибка'
    def __aver_student(self, grades):
        return round(sum(grades.values())/len(grades),1)
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__aver_student(grades)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses} "
    
        

