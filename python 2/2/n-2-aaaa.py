class person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        person.count += 1

    def get_name(self):
        print("name is %s" % (self.name))

    def get_age(self):
        print("age is %s" % self.age)

    def get_info(self):
        print("name is %s and age is %i" % (self.name, self.age))

    def brithday(self):
        self.age = self.age + 1
        print('happy birthday %s' % self.name)

    def return_count(self):
        return (person.count)


nceh = person('nceh', 25)
nceh.get_name()
# nceh.birthday()
nceh.get_age()
nceh.get_info()

print('at the moment i have %i perons' % nceh.return_count())
