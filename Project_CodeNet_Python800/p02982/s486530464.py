import math
a,b=map(int, input().split()) 
x=[list(map(int,input().split()))for _ in range(a)]
c = 0

for i in x:
    for j in x:
        ans = 0
        for k in range(b):
            ans += abs(i[k]-j[k])**2
        q = math.sqrt(ans)
        if q.is_integer() == True:
            c += 1
d = (c-a)//2
print(d)