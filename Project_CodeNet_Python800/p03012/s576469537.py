n=int(input())
a=[int(x) for x in input().split()]

b=100
for i in range(1,n):
  c=abs(sum(a[:i])-sum(a[i:]))
  if c<b:
    b=c
print(b)