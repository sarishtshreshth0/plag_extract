a=int(input())
b=list(map(int,input().split()))
d=[]
for i in range(a):
    d.append(abs(sum(b[:i])-sum(b[i:])))
print(min(d))