#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Q, H, S, D = map(int, input().split())
# N = int(input())


# In[30]:


# volume = [0.25, 0.5, 1, 2]
# unit_c = [Q*4, H*2, S, D/2]
# act_c = [Q, H, S, D]

# mylist = [[volume[i], unit_c[i], act_c[i]] for i in range(len(volume))]
# mylist_sorted = sorted(mylist, key=lambda x: x[1])

# ans = 0
# target = N
# for v,c,a in mylist_sorted:
#     count = target//v
#     ans += count*a
#     target -= v*count 
# #     print(v, c, a, count, target)
#     if target == 0:
#         break
# print(int(ans))


# In[ ]:


q, h, s, d = map(int, input().split())
n = int(input())
 
cost_per_2l = min(q*8, h*4, s*2, d)
cost_per_1l = min(q*4, h*2, s)
 
a = n // 2
b = n % 2
 
print(a*cost_per_2l + b*cost_per_1l)

