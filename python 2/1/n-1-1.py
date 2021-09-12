def maghsom(a):
    tedad = 0
    for i in range(1, a + 1):
        if a % i == 0 and:
            tedad += 1
    return tedad


b_adad = 0
b_tedad = 0
for i in range(0, 10):
    adad = int(input())
    tedad = maghsom(adad)
    if tedad > b_tedad:
        b_tedad = tedad
        b_adad = adad

print(b_adad, ' ', b_tedad)
