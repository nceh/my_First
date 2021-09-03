ageArray = []
digit = 0
maxDigit = 0
while (digit != -1):
    digit = input()
    digit = int(digit)
    if digit >= 0 and digit <=9 and digit not in ageArray:
        ageArray.append(digit)

print(ageArray)   
ageArray.sort()

avvalinMax = ageArray[len(ageArray)-1]
dovominMax = ageArray[len(ageArray)-2]

print('bozorgtaring %s ' %ageArray[len(ageArray)-1])        
print('dovomin bozorgtaring %s ' %ageArray[len(ageArray)-2])
