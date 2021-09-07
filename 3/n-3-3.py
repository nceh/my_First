def standard(name):
    name = name.lower()
    first = name[0]
    e = name[1:]
    first = first.upper()
    return first + e


nameArray = []
for item in range(0, 10):
    temp = standard((input()))
    nameArray.append(temp)

for this_one in range(0, 10):
    print(nameArray[this_one])
