from collections import OrderedDict

loghatnamee = {}
a = int(input())
for i in range(0, a):
    a, b = input().split(' ')
    loghatnamee[a] = b

loghatnamee = {"hello": "salam",
               "goodbye": "khodafez",
               "say": "goftan",
               "we": "ma",
               "you": "shoma"}

final = []

a = input()
kalamat = a.split(' ')

for item in kalamat:
    x = loghatnamee.get(item)
    if x:
        final.append(loghatnamee[item])
    else:
        final.append(item)

print(' '.join(final))
