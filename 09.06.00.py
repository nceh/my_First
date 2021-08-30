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


# In[ ]:




