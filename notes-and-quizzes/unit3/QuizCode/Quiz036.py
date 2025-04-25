#2022-01-17 Quiz 036
import pytest
class Person:
    def __init__(self, name, age):
        #print("Created Person")
        self.name = name
        self.age = age
    def get_name(self):
        if not isinstance(self.name, str):
            raise ValueError("Name must be a string")
        return self.name

    def get_age(self):
        if not isinstance(self.age, int):
            raise ValueError("Age must be an integer")
        return self.age


class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        #print("Created Student")
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Classroom():
    def __init__(self):
        self.students = []

    def add_student(self,student:Student):
        self.students.append(student)

    def remove_student(self,student:Student):
        if student not in self.students:
            raise ValueError("Student not in classroom")
        self.students.remove(student)

    def get_average_score(self):
        if len(self.students) == 0:
            raise ValueError("Classroom is empty")
        total = 0
        for student in self.students:
            total += student.get_grade()
        return total/len(self.students)


def test_student():
    student = Student("John", 20,90)
    assert student.get_name() == "John"
    assert student.get_age() == 20
    assert student.get_grade() == 90
    with pytest.raises(ValueError):
        student = Student(123, 20,90)
        student.get_name()

def test_person():
    person = Person("John", 20)
    assert person.get_name() == "John"
    assert person.get_age() == 20
    with pytest.raises(ValueError):
        person2 = Person(123, "John")
        person2.get_name()
        person2.get_age()

def test_classroom():
    classroom = Classroom()
    student1 = Student("John", 20,90)
    student2 = Student("Jane", 21,80)
    student3 = Student("Jack", 22,70)
    classroom.add_student(student1)
    classroom.add_student(student2)
    assert classroom.get_average_score() == (90+80)/2
    classroom.remove_student(student1)
    assert classroom.get_average_score() == 80
    with pytest.raises(ValueError):
        classroom.remove_student(student3)
        classroom.get_average_score()
    with pytest.raises(ValueError):
        classroom.remove_student(student1)
        classroom.remove_student(student2)
        classroom.get_average_score()




