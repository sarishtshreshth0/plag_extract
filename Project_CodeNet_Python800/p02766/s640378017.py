n,k = map(int,input().split())
c = 1
while n >= k:
    n = n // k
    c += 1
print(c)