# exm 1
# class Person:
#     def __init__(self,name,family):
#         self.name = name
#         self.family = family
#
#     def persi(self):
#         return self.name+ ' '+ self.family
#
# nceh = Person("nceh",'mousavi')
# print(nceh.family)
# print(nceh.persi())


# --------------------------------------
# exm 2
# class A:
#     def __init__(self,ram,cpu,hard):
#         self.ram = ram
#         self.cpu = cpu
#         self.hard = hard
#     def my_func(self):
#         return print("laptop man %i cpu dard va %i gig hard dard "%(self.cpu,self.hard))
#
# a =A(16,5,1000)
# print(a.my_func())


# --------------------------------------
# class Complex:
#     def __init__(self,refer,inter):
#         self.r = refer
#         self.i = inter
#
# x = Complex(2.34,34.5)
# print(x.i)
# print(x.r)

# ---------------------------------------
# class Complex:
#     def __init__(self,refer,inter):
#         self.r = refer
#         self.i = inter
#
# x = Complex(2.34,34.5)
# # print(x.i)
# # print(x.r)
# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter

# --------------------------------------

# class Dog:
#     kindly = 'nami'
#     def __init__(self,name):
#         self.n = name
#
# e = Dog('peter')
# print(e.n)
# print(e.kindly)

# -------------------------------------
# class Dog:
#     lists = []
#     def __init__(self,name):
#         self.n = name
#     def add_list(self,list):
#         self.lists.append(list)
# e = Dog('peter')
# print(e.n)
# print(e.add_list('salam'))
# print(e.lists)

# --------------------------------------

# class Dog:
#
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # creates a new empty list for each dog
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
#
# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('play dead')
# print(d.tricks)
# print(e.tricks)

# ---------------------------------------
# class Animals:
#     def __init__(self,name,cute,kindly):
#         self.n = name
#         self.c = cute
#         self.k = kindly
#         self.haappy = []
#
#     def add_happy(self,happy):
#         self.haappy.append(happy)
#
# hapoo =Animals('hapoo',10,7)
# print(hapoo.n)
# hapoo.add_happy('kheili naze')
# print(hapoo.haappy)

# ----------------------------------------
