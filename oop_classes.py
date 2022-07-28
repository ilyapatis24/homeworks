class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
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
        
    def rate_hw(self, lecturer, course, grade):
        marks = [0,1,2,3,4,5,6,7,8,9,10]
        if isinstance(lecturer, Lecturer) and grade in marks:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self,student):
        return print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {aver_stud(student)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")
    def __lt__(self, other):
        if aver_stud(self) >= aver_stud(other):
            return
        return aver_stud(self) < aver_stud(other)
def aver_lect(lecturer):
    count = 0
    countlen = 0
    for value in lecturer.grades.values():
        countlen +=len(value)
        for item in value:
            count += item
    return round(count/countlen, 2)
    
def aver_stud(student):
    count = 0
    countlen = 0
    for value in student.grades.values():
        countlen +=len(value)
        for item in value:
            count += item
    return round(count/countlen, 2)
    
class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {}     
    def __str__(self,lecturer):
        return print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {aver_lect(lecturer)}")
    def __lt__(self, other):
        if aver_lect(self) >= aver_lect(other):
            return
        return aver_lect(self) < aver_lect(other)
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def __str__(self):
        return print(f"Имя:{self.name}\nФамилия:{self.surname}")
    
lecturer1 = Lecturer("Ivan", "Petrov")
lecturer2 = Lecturer("Fedor", "Ivanov")
reviewer1 = Reviewer("Sergey", "Sidorov")
reviewer2 = Reviewer("Oleg", "Pavlov")
student1 = Student("Olga", "Filina","female")
student1.finished_courses = ["Sql", "Python"]
student1.courses_in_progress = ["C++"]
student2 = Student("Evgeniy", "Markov", "male")
student2.finished_courses = ["Php", "Golang"]
student2.courses_in_progress = ["C++"]  
lecturer1.courses_attached = ["Sql", "Python"]
lecturer2.courses_attached = ["Php", "Golang"]
reviewer1.courses_attached = ["Sql", "Python"]
reviewer2.courses_attached = ["Php", "Golang"]
student1.rate_hw(lecturer1,"Sql",9)
student1.rate_hw(lecturer1,"Python",9)
student2.rate_hw(lecturer2,"Php",8)
student2.rate_hw(lecturer2,"Golang",7)
reviewer1.rate_hw(student1, "Sql", 9)
reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Python", 8)
reviewer2.rate_hw(student2, "Php", 4)
reviewer2.rate_hw(student2, "Golang", 5)
print(student1.grades)
print(lecturer1.grades)
print(aver_lect(lecturer1))
print(aver_stud(student1))
student1.__str__(student1)
lecturer1.__str__(lecturer1)
reviewer1.__str__()
print(lecturer2.__lt__(lecturer1))
print(student2.__lt__(student1))
