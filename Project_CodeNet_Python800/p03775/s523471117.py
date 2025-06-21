#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math


# In[13]:


N = int(input())


# In[15]:


ans = len(str(N))
x = int(math.sqrt(N)//1)
a = 1
while a < x+1:
    if N%a == 0:
        b = N//a
        ans = min(ans,max(len(str(a)),len(str(b))))
    a += 1
print(ans)


# In[ ]:




