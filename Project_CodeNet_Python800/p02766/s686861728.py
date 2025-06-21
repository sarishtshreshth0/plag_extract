n,k = map(int,input().split())
a = []
while n > 0:
  a.append(n % k)
  n //= k
print(len(a))