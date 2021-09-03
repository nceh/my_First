import numpy as numpy

ageArray = []
digit = 0
maxDigit = 0
while (digit != -1):
    digit = int(input())
    if digit >= 0 and digit <=9:
        if digit > maxDigit:
            maxDigit = digit
        ageArray.append(digit)

print('bozorgtaring %s ' %maxDigit)
print('bozorgtaring ba array %s ' %max(ageArray))
print('bozorgtaring ba numpy %s ' %numpy.max(ageArray))

