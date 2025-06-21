s=input()
t=input()
a=len(s)
b=len(t)
n_list=  ['' for i in range(a)]
b_list=['' for j in range(b)]
for i in range(b) :
  if s[0] in t[:i+1] :
    b_list[i]=s[0]
for i in range(a) :
  if t[0] in s[:i+1] :
    n_list[i]=t[0]

import copy
for i in range(1,b) :
  n_list1=copy.copy(n_list)
  n_list[0]=b_list[i]
  for j in range(1,a) :

    if len(n_list1[j])>len(n_list[j]) :
      n_list[j]=n_list1[j]
    if len(n_list[j-1])>len(n_list[j]) :
      n_list[j]=n_list[j-1]
    if t[i]==s[j] and len(n_list1[j-1])+1>len(n_list[j])  :
      n_list[j] = n_list1[j - 1]+t[i]

print(n_list[-1])