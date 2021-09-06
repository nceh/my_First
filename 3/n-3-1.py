def remove(b):
    h_sedadar = ['a', 'e', 'i', 'o', 'u']
    for item in h_sedadar:
        b = b.replace(item, "")
    return b


name = input()
name = name.lower()
name = remove(name)
print(name)
words = ''
for item in range(0, len(name)):
    words += '.' + name[item]

print(words)
