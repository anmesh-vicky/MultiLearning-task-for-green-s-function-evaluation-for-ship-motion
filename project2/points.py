#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
from pannels import pannels as pl


# In[375]:


df = pd.read_csv("data.txt",header=None)
points = int(np.array(df)[0][0].split("\t")[0])


# In[362]:


p = []
for i in range(points):
    a = np.array(df)[i+1][0].split("\t")
#     print(int(a[0]))
    p.append([float(a[1]),float(a[2]),float(a[3])])
p = np.array(p)


# In[378]:


connect  =  int(np.array(df)[points+1][0].split("\t")[0])


# In[387]:


c = []
for i in range(points+1,connect+points+1):
    a = np.array(df)[i+1][0].split("\t")
#     print(int(a[0]))
    c.append([float(a[1]),float(a[2]),float(a[3]),float(a[4])])
c = np.array(c)


# In[405]:


def connect(p,c,i):
    points = []
    for z in c[i-1]:
        points.append(p[int(z-1)])
    return np.array(points)


# In[398]:


list = []
for i in range(len(c)):
    list.append(points(connect(p,c,i)))


# In[411]:


p = points(3)


# In[408]:





# In[ ]:




