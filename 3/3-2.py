def removeVowels(s):
    horoof_sedadar = ['a', 'e', 'i', 'o', 'u']
    for item in horoof_sedadar:
        s = s.replace(item, "")
        return s


str = input()
str = removeVowels(str)

tempArray = []
for item in str:
    if item != ' ':
        tempArray.append('.'+item)

# print(tempArray)
print(''.join(tempArray))
