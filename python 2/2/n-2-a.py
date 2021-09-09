lambda x: x * 2
myf = lambda x: x * 2
print(myf(3))

mylist = [1, 3, 4, 5, 7, 9]
map(lambda x: x * 2, mylist)
print(map, mylist)
print(list(map(lambda x: x * 2, mylist)))

numbers = [1, 3, 5, 89, 95, 100, 6, 8, 56, 2]
print(list(map(lambda x: 'big' if x > 10 else 'small', numbers)))

mylist = [2, 3, 5, 8, 11, 14, 17, 102, 44]
print(list(map(lambda x: 'Yes' if x % 2 == 1 else 'No', mylist)))

mylist = ['yellow', 'red', 'blue', 'red', 'yellow', 'red', 'blue', 'purple']
mylist.sort()
mylist = list(map(lambda x: 'color' if x == 'red' else x, mylist))
output = list(filter(lambda x: x == 'red', mylist))
print(output)

mylist = [2, 15, 26, 8, 11, 14, 17, 102, 44]
map_list = map(lambda x: x % 10, mylist)
filter_list = list(filter(lambda x: x <= 4, map_list))
print(filter_list)

mylist = [2, 15, 26, 8, 11, 14, 17, 102, 44]
map_list = list(map(lambda x: x % 10, mylist))
filter_list = list(filter(lambda x: x <= 4, map_list))
print(filter_list)

mylist = [2, 15, 26, 8, 11, 14, 17, 102, 44]
map_list = list(map(lambda x: x % 5, mylist))
filter_list = list(filter(lambda x: x < 4, map_list))
print(filter_list)

mylist = [2, 15, 26, 8, 11, 14, 17, 102, 44]
map_list = list(map(lambda x: x % 10, mylist))
filter_list = filter(lambda x: x <= 4, map_list)
print(filter_list)

mylist = [1, 4, 5, 6, 7, 8, 98, 45]
print(list(filter(lambda x: x % 2 == 0, mylist)))

x = 10
print(x % 5)
