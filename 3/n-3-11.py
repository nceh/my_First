from collections import OrderedDict

ara_list = []
ara_dict = {}
totalN = int(input())
for item in range(0, totalN):
    ara_list.append(input())

for this_one in ara_list:
    ara_dict[this_one] = ara_dict.get(this_one, 0) + 1

names = list(ara_dict.keys())
names = sorted(names)

for i in names:
    print(i, " ", ara_dict[i])
