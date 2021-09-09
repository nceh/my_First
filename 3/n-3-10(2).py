n = int(input())
quality = []
price = []
count = 0
for i in range(0, n):
    laptop_qp = input()
    quality_price = laptop_qp.split()
    quality.append(quality_price[0])
    price.append(quality_price[1])
for j in range(0, len(price)):
    a = int(price.pop(0))
    b = int(quality.pop(0))
    for k in range(0, len(price)):
        if (a < int(price[k]) and b > int(quality[k])) or (int(price[k]) < a
                                                           and int(quality[k]) > b):
            count = count + 1
if count > 0:
    print('happy irsa')
else:
    print('poor irsa')
