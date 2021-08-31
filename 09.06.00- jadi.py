#!/usr/bin/env python
# coding: utf-8

# In[3]:


reshte = input()
reshte.lower()
reshte=reshte.replace("a","")
reshte=reshte.replace("e","")
reshte=reshte.replace("i","")
reshte=reshte.replace("o","")
reshte=reshte.replace("u","")
# print(reshte)

khoroji=""
for i in range(0,len(reshte)):
    khoroji +="."+reshte[i]
print(khoroji)


# In[53]:


#moahkelsh hal nashod
vorodi = (input())
print(vorodi)
vorodi=vorodi.replace("+",",")


vorodi=vorodi.split(",")
a =int(vorodi)
a
# a=[]
# a.append((vorodi))
# a




# a = []
# a.append(vorodi)
# a.sort()
# for i in a:
#     print(i)


# In[17]:


def standard(name):
    sta=name[0].upper()+name[1:]
    return sta
# standard("ali")
for i in range(0,10):
    name = input("please enter your name: ")
    print(standard(name))


# In[ ]:


def estandard(a):
    a=a.lower()
    first= a[0]
    edame= a[1::]
    first=first.upper()
    return first+edame
list= []
for i in range(0,10):
    temp=estandard(input())
    list.append(temp)
    
for j in range(0,10):
    print(list[j])


# In[19]:


def standard(name):
    sta=name[0].upper()+name[1:]
    return sta

list= []
for i in range(0,10):
    temp=standard(input())
    list.append(temp)
    
for j in range(0,10):
    print(list[j])


# In[ ]:


a= input()
a=a.lower()
vaziat = "NO"
if ('h' in a) and ("e" in a) and ("ll") and ("o" in a):
    vaziat="YES"
else:
    vaziat = "NO"
    
    
h=a.find('h')
e=a.find('e')
ll=a.find('ll')
o=a.find('o')

if vaziat=='YES' and o>ll and ll>e and e>h:
    vaziat= "YES"
else:
    vaziat="NO"
    
print(vaziat)


# In[21]:


a = input()
a=a.lower()
vaziat = "NO"
if ("h" in a) and ("e" in a) and ("ll" in a) and ("o" in a):
    vaziat = "YES"
else:
    vaziat = "NO"

h = a.find("h")
e = a.find("e")
ll = a.find("ll")
o = a.find("o")

if vaziat =="YES" and o>ll and ll>e and e>h:
    vaziat = "YES"
else:
    vaziat = "NO"

print(vaziat)


# In[41]:


string = input()
# string = string.replace("AB","@")
# string = string.replace("BA","$")
# vaziat =""
if ("AB" in string) and ("BA" in string):
    vaziat = "YES"
else:
    vaziat = "NO"
    
print(vaziat)


# In[48]:


l = [1,3,4,5,6]
for i in range(0,(len(l))):
    print(i,l[i])


# In[55]:


s = input()
x1,x2,x3 = s.split(" ")
# print(x1,x2,x3)
x1= int(x1)
x2=int(x2)
x3=int(x3)

print(max(x1,x2,x3) - min(x1,x2,x3))


# In[2]:


a = input()
b = [int(l) for l in input().split(" ")]
temp=[]
for i in range (0,len(b)):
    temp.append(b[i])
    
count=0
for j in range(0,len(temp)):
    if temp[j]==0 or temp[j]==1 or temp[j]==2:
        count+=1
print(int(count/3))


# ###### dictionary

# In[5]:


string = "salam nceh, halet chetore?"
count = dict()
for letter in string:
    if letter in count:
        count[letter] +=1
    else:
        count[letter] =1
    
    print(letter,count)


# In[6]:


string = "nceh salam, chetorii? khobi?"
count = dict()

for letter in string:
    if letter in count:
        count[letter] +=1
    else:
        count[letter] = 1
        
for this_one in list(count.keys()):
    print("%s appeard %s times" % (this_one,count[this_one]))


# In[7]:


string = "nceh salam, chetorii? khobi?"
count = dict()

for letter in string:
    count[letter] = count.get(letter,0)+1
        
for this_one in list(count.keys()):
    print("%s appeard %s times" % (this_one,count[this_one]))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[29]:


def lo_counter(a):
    l_counter=0
    lo=a.lower()
    for i in range (0,int(len(a))):
        if a[i]==lo[i]:
            l_counter+=1
    return l_counter
def up_counter(b):
    u_counter=0
    up=a.upper()
    for j in range (0,int(len(a))):
        if a[j]==up[j]:
            u_counter+=1
    return u_counter
a= input()
vaziat=True

if lo_counter(a) == up_counter(a):
    vaziat=True
if lo_counter(a) > up_counter(a):
    vaziat=True
if lo_counter(a) < up_counter(a):
    vaziat=False
if vaziat:
    a=a.lower()
else:
    a=a.upper()
print(a)


# In[33]:


def lo_counter(a):
    l_counter = 0 
    lo=a.lower()
    for i in range(0,int(len(a))):
        if a[i] ==lo[i]:
            l_counter +=1
    return l_counter

def up_counter(a):
    u_counter = 0
    up = a.upper()
    for j in range(0,int(len(a))):
        if a[j] == up[j]:
            u_counetr +=1
    return u_counter

a = input()
vaziat = True
if lo_counter(a) == up_counter(a):
    vaziat = True
elif lo_counter(a) > up_counter(a):
    vaziat = True
else:
    vaziat = False
    
if vaziat == True:
    a = a.lower()
else:
    a = a.upper()
print(a)


# In[ ]:


def palindrome(a):
    lenny=len(a)
    vaziat=True
    temp=a[::-1]
    for i in range (0,lenny):
        if a[i]!=temp[i]:
            vaziat=False
            
    return vaziat


a=input()
a=a.lower()

if palindrome(a):
    print("palindrome")
    
else:
    print("not palindrome")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




