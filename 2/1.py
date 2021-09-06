def divi(a):
    tedad = 0
    for i in range(1, a + 1):
        if (a % i) == 0:
            tedad += 1
    return tedad


for i in range(0, 20):
    number = int(input())
    tedad = divi(number)
