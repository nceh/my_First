from math import sqrt
from itertools import count, islice

def is_prime(n):
    if n < 2:
        print('not prime')
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
             print('not prime')
             return False

    print('prime')
    return True



digit = '0';
while (digit != 'c'):
    digit = input()
    if digit == 'c': 
        break;
    else: 
        is_prime((int(digit)))