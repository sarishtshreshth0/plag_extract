n=int(input())
a=[int(x) for x in input().split()]

b=10000
for i in range(n):
  c=(sum(a[:i+1])-sum(a[i+1:]))**2
  if c<b:
    b=c
print(int(b**0.5))