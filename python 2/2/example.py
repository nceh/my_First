# # a = [1, 2, 3, 4]
# # print(sum(a))
#
# import math
#
# def divisorGenerator(n):
#     large_divisors = []
#     for i in range(1, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             yield i
#             if i*i != n:
#                 large_divisors.append(n / i)
#     for divisor in reversed(large_divisors):
#         yield divisor
#
# def prime(m):
#     if m > 1:
#         for i in range(2, int(m / 2) + 1):
#             if (m % i) == 0:
#
#
#
#
# print(list(divisorGenerator(100)))
# for item in range(0,10):
#     adad = int(input())
#     adadT = divisorGenerator(adad)
#     if adadT


# import csv
#
# with open('Book1.csv') as f2:
#     reader = csv.reader(f2)
#     for row in reader:
#         print(row)


import csv


class Customer:
    def __init__(self, name, nationalcode, sumpurchase):
        self.name = name
        self.nationalcode = nationalcode
        self.sumpurchase = sumpurchase


class_customers = []

with open('Book1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        customerObj = Customer(row[0], row[1], row[2])
        class_customers.append(customerObj)
        print(row)
