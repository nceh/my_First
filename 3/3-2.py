digitArray = []
digit = 0
while (digit != -1):
    digit = input()
    digit = int(digit)
    if digit >= 0:
        digitArray.append(digit)

digitArray.sort()

# for i in digitArray:
#     print(i)
print(digitArray)
