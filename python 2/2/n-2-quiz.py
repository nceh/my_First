# class maktabkhooneh:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         print("my name is %s and my age is %i" % (self.name, self.age))
#
#
# Maktabkhooneh = maktabkhooneh('maktabkhooneh', 7)
#
# Maktabkhooneh.get_name()


# class university:
#     def __init__(student, name, number_of_grade, grade1, grade2, grade3):
#         student.name = name
#         student.number_of_grade = number_of_grade
#         student.grade1 = grade1
#         student.grade2 = grade2
#         student.grade3 = grade3
#
#     def get_name(student):
#         print("Student name is %s" % student.name)
#
#     def get_grades(student):
#         total_grade = student.grade1 + student.grade2 + student.grade3
#         average = total_grade / student.number_of_grade
#         print("The Average is %i" % average)
#
#
# Information = university("Hossein", 3, 16, 12, 18)
# Information.get_name()
# Information.get_grades()


# color = input()


# class Vehicle:
#     def __init__(model, name, color):
#         model.name = name
#         model.color = color
#
#     def get_name(model):
#         print("Vehicle name is %s" % model.name)
#
#     def get_color(model):
#         print("Vehicle color is %s" % model.color)
#
#
# Information = Vehicle("Hossein", color)
# Information.get_name()
# Information.get_color()

# class Vehicle:
#     color = input()
#
#     def __init__(model, name, color):
#         model.name = name
#         model.color = color
#
#     def get_name(model):
#         print("Vehicle name is %s" % model.name)
#
#     def get_color(model):
#         print("Vehicle color is %s" % model.color)
#
#
# Information = Vehicle("Hossein", color)
# Information.get_name()
# Information.get_color()


# class Vehicle:
#     def __init__(model, name):
#         model.name = name
#
#     def get_name(model):
#         print("Vehicle name is %s" % model.name)
#
#     def get_color(model):
#         color = input()
#         print("Vehicle color is %s" % color)
#
#
# Information = Vehicle("Hossein")
# Information.get_name()
# Information.get_color()


# class maktabkhooneh:
#     def __init__(self, name, grade, age):
#         self.name = name
#         self.grade = grade
#         self.age = age
#
#     def value(self):
#         return self.name + self.grade
#
#
# person = maktabkhooneh("Ahmad", "Master", 24)
# print(person.value())


class mobile:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def get_name(self):
        return self.name


class cpu(mobile):
    def get_name(self):
        print("This mobile has HighTech %s CPU " % self.name)


brand = cpu("Intel", "Sony")
print(brand.get_name())
