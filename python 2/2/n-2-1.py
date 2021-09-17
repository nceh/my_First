class Student:
    ghad = 0
    vazn = 0
    sen = 0

    def __init__(self, ghad, vazn, sen):
        self.ghad = ghad
        self.vazn = vazn
        self.sen = sen


class School:
    students = []

    def setStudents(self, count):
        pass

    def calcAvg(self):
        pass


count1 = int(input())
schoolA = School
schoolA.setStudents(count1)
count2 = int(input())
schoolB = School
schoolB.setStudents(count2)
