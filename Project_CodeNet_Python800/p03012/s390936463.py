n = int(input())
w = list(map(int,input().split()))
a = 0
b = sum(w)
kai = b-a
ichizi = 0
for i in range(n):
  a +=w[i]
  b -=w[i]
  ichizi = abs(a-b)
  kai = min(kai,ichizi)
print(kai)