#!/usr/bin/env python
# coding: utf-8

# # مترجم آنلاین - فصل 3

# In[ ]:


from collections import OrderedDict
ara_list=[]
ara_dic={}

tedad=int(input())
for i in range (0,tedad):
    ara_list.append(input())
    
for item in ara_list:
    if item in ara_dic.keys():
        ara_dic[item]=ara_dic[item]+1
    else:
        ara_dic[item] =1
        
asami =list(ara_dic.keys())
asami= sorted(asami)

for h in asami:
    print(h, " ",ara_dic[h])


# In[4]:


from collections import OrderedDict
ara_list=[]
ara_dic={}

tedad=int(input())
for i in range(0,tedad):
    ara_list.append(input())
    
for item in ara_list:
    ara_dic[item]= ara_dic.get(item,0) + 1
    
asami = list(ara_dic.keys())
asami = sorted(asami)

for this_one in asami:
    print(this_one ," ", ara_dic[this_one])


# In[15]:


vazn = {"ali" : 50 , "sara" : 56 , "nima" :80}
vazn.items()


# In[16]:


list(vazn.items())


# In[17]:


for name,vazn in list(vazn.items()):
    print("vazn %s hastesh %s kilo " %(name,vazn))


# In[18]:


fin = open("salam.txt")


# In[19]:


fin


# In[20]:


fin.read()


# In[21]:


fin.read()


# In[24]:


type(fin)


# In[25]:


fin.close()


# In[26]:


type(fin)


# In[27]:


fin = open("salam.txt")


# In[28]:


for line in fin:
    print(line)


# In[13]:


fin = open("salam.txt")
# fin.read()
counter = 0
for line in fin:
    counter +=1
    print("line number %i is : %s" %(counter,line))


# In[7]:


a = ''' 12
'''
a


# In[8]:


print(a)


# In[9]:


a.strip()


# In[10]:


fin = open("salam.txt")
for line in fin:
    print(line.strip())


# In[14]:


f = open("salam.txt")
counter=sum = 0
for line in f:
    counter+=1
    this_one=float(line.strip())
    sum += this_one
    
a=sum/counter    


# In[15]:


a


# In[22]:


f = open("salam.txt")
f.readlines()


# In[20]:


f = open("salam.txt")
lines=f.readlines()

for line in lines:
    print(line.strip())


# In[24]:


f1 = open("avarage.txt", 'w')
f1


# In[28]:


avarage= sum/counter
avarage
f1.write(str(avarage))


# In[30]:


avarage=str(avarage)
f1.write(avarage)
type(f1
    )


# In[32]:


from random import randint

def randomFn(min , max):
    rand = randint(min,max) 
    print("my random digit is: " , rand)
    return rand


res = ""
min = 0
max = 99
while res != "d":
    rand = randomFn(min,max)
    res = input("enter >> ")
    if (res == "d"):
        print("Yeeeeeeeeesssss")
        break
    elif res == "k":
        max = rand - 1
    elif res == "b":
        min = rand + 1


# In[ ]:


loghatnamee={}
a = int(input())
for i in range (0,a):
    a,b= input().split(' ')
    loghatnamee[a]=b
    


# In[ ]:




