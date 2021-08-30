#!/usr/bin/env python
# coding: utf-8

# In[1]:


name= input("please enter your name: ")
if name =="nceh":
    print("salam nceh")
elif name == "jadi":
    print("salam jadi")
else: 
    print("salam gharibe")


# In[6]:


adad= (input())
yekan = adad[2]
dahgan = adad[1]
sadgan = adad[0]
adad=int(yekan + dahgan+sadgan)*2
print(adad)


# In[9]:


adad= int(input())
a = adad%10
b= (adad-a)+10
print(b)


# In[10]:


def salambye(name):
    print("salam" , name)
    print("bye bye" , name)
salambye("nceh")


# In[11]:


def jam(a,b):
    javab=a+b
    return javab
jam(2,3)


# In[21]:


hour= int(input())
per_hour = int(input())
def hoghogh(hour,per_hour):
    if hour > 8:
        return "error"
    elif per_hour< 10:
        return "boro khonaton"
    else: 
        daramad = hour*per_hour
        return daramad
print(hoghogh(hour,per_hour))


# In[22]:


n = 5
while n>0:
    print(n)
    n -=1


# In[23]:


name = input("what is your name? ")
while name != "end":
    print("salam", name)
    name = input("what is your name? ")


# In[24]:


n = 3
while n>0:
    print(n)
    n +=1
    if n == 100:
        break


# In[25]:


friends= ["ali",'reza','mina']
for thisone in friends:
    print("salam",thisone)


# In[26]:


friends= ["ali",'reza','mina']
count = 0
for thisone in friends:
    print("salam",thisone)
    count+=1
print(" i say" , count, "hellos")


# In[ ]:


adad = int(input())
count = 0
sum = 0
while 1:
    adad != -1
    count+=1
    sum = sum+adad
    adad=int(input())
    
avrage = count/sum
print(avrage)


# In[2]:


count = 0
sum = 0
while True:
    adad = int(input())
    if adad != -1:
        count +=1
        sum =sum+adad
    else:
        break
avrage =sum/count
print(avrage)


# In[9]:


from random import randint
adad = randint(1,99)
hads = int(input())
while hads != adad:
    if hads >adad:
        print("adad kochektar bezan")
    else: 
        print("adad bozorgtar bezn")
    hads = int(input())

print(" afariiin tu dorost gooooftiii") 


# In[11]:


from random import randint
adad = randint(1,99)
name = input("please enter your name: ")
hads = int(input())
while hads != adad:
    if hads >adad:
        print("adad kochektar bezan")
    else: 
        print("adad bozorgtar bezn")
    hads = int(input())

print(" afariiin", name, "dorost gooooftiii") 


# In[16]:


adad = int(input())
for i in range(2,adad):
    if (adad %i) == 0:
        print("not prime")
    else:
        print("prime")
        break


# In[ ]:


# barasi aval bodan adad

import math
a=int(input())
pri = 'prime'
for i in range(2,a):
    if (a%i)==0:
        pri='not prime'
        break
        
print(pri)


# In[20]:


# import math 
a = int(input())
pri = "prime"
for i in range(2,a):
    if (a%i)==0:
        pri="not prime"
        break
print(pri)


# In[21]:


emt= int(input())
jamemt=0
tedadbord=0
for i in range(1,30):
    if emt == 3:
        tedadbord+=1 
        jamemt=jamemt+emt
    else:
        jamemt=jamemt+emt

print(jamemt," ", tedadbord)
        


# In[ ]:


sum1=0
win_counter=0
for i in range (0,30):
    vorodi=int(input())
    sum1+=vorodi
    
    if vorodi==3:
        win_counter+=1
        
print(sum1,' ',win_counter)


# In[ ]:


sum =0
win = 0
for i in range(0,30):
    adad=int(input())
    sum +=adad
    if adad == 3 :
        win +=1
        
print(sum, " ", win)


# In[2]:


sen = int(input())
list1 = []
list1.append(sen)
while sen != -1:
    sen=int(input())
    list1.append(sen)
        
list1.sort()
print(list1[-1])
   


# In[5]:


adad=int(input())
a=[]
a.append(adad)
while(adad !=-1):
    adad=int(input())
    a.append(adad)
    
    
a.sort()
print(a[-1],a[-2])


# In[4]:


from math import sqrt
tedad= int(input())
def sqr(adad):
    rishe = sqrt(adad)
    return rishe
for i in range(0,tedad):
    adad= float(input())
    print(sqr(adad))
    


# In[3]:


def maghsom(a):
    tedad=0
    for i in range (1,a+1):
        if(a%i)==0:
            tedad+=1
    return(tedad)

b_adad=0
b_tedad=0
for i in range(0,20):
    adad=int(input())
    tedad=maghsom(adad)
    if tedad>b_tedad:
        b_tedad=tedad
        b_adad=adad
        
print(b_adad,' ',b_tedad)


# In[2]:


def maghsom(a):
    tedad=0
    for i in range(1,a+1):
        if (a%1)==0:
            tedad+=1
    return (tedad)

maghsom(12)
# badad=0
# btedad=0
# for i in range(0,20):
#     adad=int(input())
#     tedad=maghsom(adad)

# print(maghsom(adad))
            


# In[5]:


a = 'salam azizam'
for i in range (0,len(a)):
    print(a[i])


# In[6]:


for letter in "my string":
    print(letter)


# In[8]:


name = "my name is nceh"
count= 0
for harf in name:
    if harf=="n":
        count+=1
        
count


# In[9]:


name[:3]


# In[10]:


name[:-3]


# In[11]:


name[-3:]


# In[13]:


name = "M"+name[1:]
name


# In[14]:


"a" in "nceh"


# In[15]:


dir("nceh")


# In[16]:


name.find("n")


# In[18]:


name.startswith("M")


# In[19]:


name = "ali"
sen = 20
print("hello %s midoni %i sale shodi?" % (name,sen))


# In[21]:


friends = ["ali" ,"reza","shima"]
for thisone in friends:
    print("salam %s" % thisone)


# In[ ]:




