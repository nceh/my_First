number_of_laptops = int(input())
list_of_prices = []
list_of_qualities = []

for i in range(0, number_of_laptops):
    inp = input()
    numbers = []
    numbers = [int(s) for s in inp.split() if s.isdigit()]
    list_of_prices.append(numbers[0])
    list_of_qualities.append(numbers[1])


def find_better_lp(number_of_laptops):

if number_of_laptops == 0:
    return print("empty list")

for i in range(0, number_of_laptops):
    for j in range(0, number_of_laptops):
        if ((list_of_prices[i] <= list_of_prices[j]) and i != j):
            if (list_of_qualities[i] >= list_of_qualities[j]):
                return print("happy irsa")

return print("poor irsa")

find_better_lp(number_of_laptops)
