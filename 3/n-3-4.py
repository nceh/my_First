str = input()
str = str.lower()

vaziat = 'NO'
if ('h' in str) and ('e' in str) and ('ll' in str) and ('o' in str):
    vaziat = 'YES'
else:
    vaziat = 'NO'

h = str.find('h')
e = str.find('e')
ll = str.find('ll')
o = str.find('o')

if vaziat == "YES" and o > ll and ll > e and e > h:
    vaziat = "YES"
else:
    vaziat = "NO"

print(vaziat)
