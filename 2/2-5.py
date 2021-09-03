def divisor(n):
  x = len([i for i in range(1,n+1) if not n % i])
  return x


digitArray = []
divisorArray = []
digit = -1
while (len(digitArray) <= 5):
    digit = int(input())
    if len(digitArray) < 5:
      digitArray.append((int(digit)))  
      divisorArray.append(divisor(int(digit)))  
      # print(digitArray)
    elif len(digitArray) == 5: 
      # divisor(digitArray)
      break

# print(divisorArray)
maxDivisor = max(divisorArray)
index = divisorArray.index(maxDivisor)

print('add ==> %s ' %digitArray[index])
print('tedad ==> %s ' %maxDivisor)


# while (len(digitArray) <= 5):
#     digit = int(input())
#     if len(digitArray) < 5:
#       digitArray.append((int(digit), divisor(int(digit))))  
#       print(digitArray)
#     elif len(digitArray) == 5: 
#       # divisor(digitArray)
#       break

# print(digitArray)