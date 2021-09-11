class A:
    n = int(input())
    count = 0
    list_ghad = []
    list_vazn = []
    list_sen = []

    def __init__(self, ghad, vazn, sen):
        self.ghad = ghad
        self.vazn = vazn
        self.sen = sen

    def get_ghad(self):
        list_ghad.append(ghad)
        sum = sum(list_ghad)

        average = sum / n
        print("The Average is %i" % average)


nceh = A(165, 48, 25)

# class B(A):
#     t = int(input())
