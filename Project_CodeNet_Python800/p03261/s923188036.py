from collections import defaultdict
d = defaultdict(int)
N=int(input())
s=input()
d[s]+=1
x=s[-1]
for i in range(N-1):
  s=input()
  if s[0]==x and d[s]==0:
    x=s[-1]
    d[s]+=1
  else:
    print('No')
    exit(0)
print('Yes')