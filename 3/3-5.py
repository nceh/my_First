str = input()

lowerCounts = 0
upperCounts = 0

for s in str:
    if s.islower():
        lowerCounts += 1
    elif s.isupper():
        upperCounts += 1

# print(lowerCounts)
# print(upperCounts)
if lowerCounts >= upperCounts:
    print(str.lower())
else:
    print(str.upper())
