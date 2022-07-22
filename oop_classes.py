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
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else:
            return 'Ошибка'
    def aver_student(self):
        return round(sum(self.grades.values())/len(self.grades),1)
    def __str__(self):
        return print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.aver_student()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")
    def __lt__(self, other):
        if self.aver_student() >= other.aver_student():
            return
        return self.aver_student() < other.aver_student()
    
class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {}     
    def aver_lect(self):
        return round(sum(self.grades.values())/len(self.grades),1)
    def __str__(self):
        return print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.aver_lect()}")
    def __lt__(self, other):
        if self.aver_lect() >= other.aver_lect():
            return
        return self.aver_lect() < other.aver_lect()
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
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
print(student1.aver_student())
print(lecturer1.aver_lect())
print(student2.aver_student())
print(lecturer2.aver_lect())
student1.__str__()
lecturer1.__str__()
reviewer1.__str__()
print(lecturer2.__lt__(lecturer1))
print(student2.__lt__(student1))
