# from collections import OrderDict

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
