import pytest
from Quiz036 import Student
from Quiz036 import Classroom

def test_add_student():
    classroom = Classroom()
    student = Student("John", 18, 90)
    classroom.add_student(student)
    assert student in classroom.students

def test_remove_student():
    classroom = Classroom()
    student = Student("John", 18, 90)
    classroom.add_student(student)
    classroom.remove_student(student)
    assert student not in classroom.students

def test_remove_non_existing_student():
    classroom = Classroom()
    student = Student("John", 18, 90)
    with pytest.raises(ValueError):
        classroom.remove_student(student)

def test_get_average_score():
    classroom = Classroom()
    student1 = Student("John", 18, 90)
    student2 = Student("Jane", 19, 80)
    classroom.add_student(student1)
    classroom.add_student(student2)
    assert classroom.get_average_score() == (90 + 80) / 2

def test_empty_classroom():
    classroom = Classroom()
    with pytest.raises(ValueError):
        classroom.get_average_score()
