n=int(input());a=list(map(int,input().split()));m=float('inf')
for i in range(1,n): m=min(m,abs(sum(a[:i])-sum(a[i:])))
print(m)