# function which return reverse of a string

# def isPalindrome(s):
#     return s == s[::-1]


def func(s):
    # Run loop from 0 to len/2
    if 'AB' in s and 'BA' in s and 'ABA' not in s and 'BAB' not in s:
        return True
    else:
        return False


# Driver code
strInput = input()
ans = func(strInput)

if ans:
    print("YES")
else:
    print("NO")
