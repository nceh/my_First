def str(a):
    if ('AB' in a) and ('BA' in a):
        return True
    else:
        return False


userinp = input()

user = str(userinp)
if user:
    print('YES')
else:
    print('NO')
