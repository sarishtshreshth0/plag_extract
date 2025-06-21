n,k = map(int, input().split())
res = 0
m = n-1
a = 1
while True:
    if n <= k**a - 1:
        break
    a += 1
print(a)