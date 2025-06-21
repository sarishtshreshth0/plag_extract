n, k = map(int, input().split())
ret = 1
while n // k != 0:
    ret += 1
    n = n // k
print(ret)