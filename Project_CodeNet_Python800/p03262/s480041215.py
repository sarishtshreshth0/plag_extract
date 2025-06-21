#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
from functools import reduce


# In[15]:


N,X = map(int, input().split())
x = list(map(int, input().split()))


# In[16]:


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


# In[17]:


def myfunc(x,X):
    mylist = [abs(i-X) for i in x]
    print(gcd_list(list(set(mylist))))


# In[18]:


myfunc(x,X)


# In[ ]:




