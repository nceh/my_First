# number = int(input())
numberArray = []
number = 0
while (number != -1):
    number = int(input())
    if number >= 0 and number <= 3:
        numberArray.append(number)

numberArray.sort()

print(numberArray)
