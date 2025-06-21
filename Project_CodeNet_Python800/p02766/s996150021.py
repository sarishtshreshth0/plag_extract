n, base = map(int, input().split())
ret = 0
while n:
    n //= base
    ret += 1
print(ret)