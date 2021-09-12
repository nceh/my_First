# import csv
# f = open("electronic-card-transactions-aug-2021-csv-tables.csv")
# # print(f.read())
# # print(f.read(6))    # che tedad karakter bekhone
# #------------------------------------
# # # تابع readline برای خواندن خط به خط فایل
# # print(f.readline())
# # print(f.readline())
# -------------------------------------
# # تابع readlines
# # print(f.readlines())
# -------------------------------------
# # استفاده از حلقه برای خواندن فایل
#
# # for line in f:
# #     print(line)
# -------------------------------------
# # بستن فایل پس از کار با فایل
# f.close()
# --------------------------------------

# نوشتن فایل

# file1 = 'nceh.csv'
# f = open(file1, 'w')
# f.write('hello word')


# ---------------------------------------
# writelines
# f = open('nceh.csv','w')
# f.writelines(['salam azizam\n', 'hi'] )
# f.close()

# ---------------------------------------
# اضافه کردن محتوا به محتوای موجود در فایل (a)
# f = open('nceh.csv','a')
# f.writelines([' \nazizam\n', 'hi baby'] )
# f.close()

# ---------------------------------------
# حذف فایل
# import os
# os.remove('nceh.csv')
#
# or ------------------------------------
# if os.path.exists("delete_file.txt"):
#     os.remove("delete_file.txt")

# ---------------------------------------
# try:
#     open("testFile.txt")
# except:
#     print("An Error Occurred While Opening File!")
# ---------------------------------------
# try:
#     num = int( input("Please enter the number: ") )
#     print( num**2 )
# except ValueError:
#     print("لطفا در ورودي فقط عدد وارد کنيد!")

# ---------------------------------------
# try:
#     num = int( input("Please enter the number: ") )
#     print( num**2 )
# except ValueError:
#     print("لطفا در ورودي فقط عدد وارد کنيد!")
# finally:
#     print("Ended!")

# هر فرآیند مدیریت خطا در پایتون فقط می‌تواند شامل یک بخش try و یک بخش finally باشد؛ اما می‌تواند except های متعددی برای انواع خطاها داشته باشد.
# ---------------------------------------
# try:
#     f = 'file.text'
#     f = open("file.txt")
#     f.write("Test from SabzDanesh.com")
# except:
#     print("Something went wrong when writing to the file!")
# finally:
#     f.close()
# ---------------------------------------
try:
    f = open('file.txt')
    s = f.readline()
    i = int(s.strip())
except OSError:
    print("We have OS error!")
except ValueError:
    print("Could not convert data to an integer!")
except:
    print("Unexpected error!")
