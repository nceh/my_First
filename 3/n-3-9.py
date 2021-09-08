total = input()
numberP = [int(l) for l in input().split(' ')]
# print(numberP)
count = 0
for this_one in range(0, len(numberP)):
    if numberP[this_one] == 0 or numberP[this_one] == 1 or numberP[this_one] == 2:
        count += 1

print(int(count / 3))
