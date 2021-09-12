# class Employee:
#     empcount = 0
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Employee.empcount +=1


# ----------------------------------------------------------------
# فراخانی کلاس در پایتون

class Person:
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def print_person_profile(self):
        print('name:', self.name)
        print('age: ', self.age)


person = Person('nceh', 25)
print(person.print_person_profile())
