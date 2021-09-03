nameArray = []
name = ''
while len(nameArray) < 3:
    name = input()
    if len(nameArray) < 3:
        if len(name) >= 3:
            nameArray.append(name.lower())

result = []
for name in nameArray:
    result.append(name.capitalize())
print(result)
