def calculate(arr):
   total_scores = sum(arr)
   count = 0;
   for score in arr:
       if (score == 3):
           count = count +1 
   print('jame emtiazat: %s ' % total_scores)
   print('jame bord ha: %s ' % count)



scoresArray = []
digit = -1
while (len(scoresArray) <= 5):
    digit = int(input())
    if digit == 0 or digit == 1 or digit == 3:
        if len(scoresArray) < 5:
            scoresArray.append(int(digit))  
            print(scoresArray)
        elif len(scoresArray) == 5: 
            calculate(scoresArray)
            break