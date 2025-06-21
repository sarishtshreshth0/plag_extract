n=int(input())
l=[]

for i in range(n):
  x_=input()
  if x_ not in l:
    l.append(x_)
    
  else:
    print('No')
    exit()
    
alpha_list=[chr(i) for i in range(97,123)]

for i in range(len(l)-1):
  if l[i][-1]==l[i+1][0]:
    continue
    
  else:
    print('No')
    exit()
    
print('Yes')