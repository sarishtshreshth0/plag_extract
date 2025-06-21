n,k = map(int,input().split())
c = 0
while n >= k:
    n = n // k
    c = c + 1

print(c + 1)