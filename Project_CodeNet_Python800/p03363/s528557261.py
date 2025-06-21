from collections import Counter    
a=[0]
n=int(input())
p=0
for i in input().split():
    p+=int(i)
    a.append(p)

c=Counter(a)
ans=0
for i in list(c.values()):
    ans+=i*(i-1)//2
print(ans)
