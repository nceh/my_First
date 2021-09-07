letter = input()
lowercounts = 0
uppercounts = 0

for l in letter:
    if l.islower():
        lowercounts += 1
    elif l.isupper():
        uppercounts += 1

if lowercounts >= uppercounts:
    print(letter.lower())
else:
    print(letter.upper())
