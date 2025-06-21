a, b = map(int, input().split())


def F(x):
    res = 0
    p, q = divmod(x+1, 2)
    if q:
        res ^= x
    if p % 2:
        res ^= 1
    return res
  

print(F(b) ^ F(a-1))