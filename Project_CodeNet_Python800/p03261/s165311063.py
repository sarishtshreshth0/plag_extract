#!/usr/bin/env python
# coding: utf-8

# In[10]:


N = int(input())
W = []
for _ in range(N):
    W.append(input())


# In[11]:


if len(set(W)) != N:
    print("No")
else:
    for i,word in enumerate(W):
        if i > 0:
            if W[i-1][-1] != word[0]:
                print("No")
                break
    else:
        print("Yes")


# In[ ]:




