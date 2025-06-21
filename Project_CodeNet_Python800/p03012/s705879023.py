n=int(input())
*w,=map(int,input().split())
l=[]
for i in range(n):
    l.append(abs(sum(w[:i+1])-sum(w[i+1:])))
print(min(l))