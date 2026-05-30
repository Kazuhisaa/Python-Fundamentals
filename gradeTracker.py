import os 
import json

FILENAME = "grades.json"


def save_student_grades(grades):
    with open(FILENAME, 'w')as f:
        json.dump(grades,f)


def add_student_grades(grades):
    entry = {
        "name": input("What is the students name? "),
        "grade": float(input("What is the grade? ")),
        "section": input("What is Students section")
    }
    grades.append(entry)
    save_student_grades(grades)


if __name__== "main":
    print("======================")
    print("=    Grade Tracker   =")
    print("======================")
    print("/n 1. Add Student Grades")
    print("2. View Student Grades")
    print("3. Calculate Student Grade")
    print("4. Exit")
    choice = int(input("Please choose a number: " ))