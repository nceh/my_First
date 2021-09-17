# Python3 code to  calculate age in years

import datetime


# inp = input()


def validate(date):
    try:
        datetime.datetime.strptime(date, '%Y/%m/%d')
        dataParams = date.split('/')
        if len(dataParams[0]) != 4 or len(dataParams[1]) != 2 or len(dataParams[2]) != 2:
            return False
        return True
    except ValueError:
        return False


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year
    ((today.month, today.day) <
     (birthDate.month, birthDate.day))
    return age


date = input()
if validate(date):
    dataParams = date.split('/')
    print(calculateAge(datetime.date(int(dataParams[0]), int(dataParams[1]), int(dataParams[2]))))
else:
    print("WRONG")
