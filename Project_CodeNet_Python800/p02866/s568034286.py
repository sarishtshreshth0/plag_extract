#!/usr/bin/env python
# coding: utf-8

# In[4]:


import collections


# In[2]:


N = int(input())
D = list(map(int, input().split()))


# In[7]:


mod = 998244353
if D[0] == 0:
    ans = 1
    tmp = 1
    cnt = 0
    for i,x in sorted(collections.Counter(D[1:]).items(), key=lambda x:x[0]):
        if i == cnt+1:
            ans *= (tmp**x)%mod
            tmp = x
            cnt += 1
        else:
            ans = 0
            break
    print(ans%mod)
else:
    print(0)


# In[ ]:




