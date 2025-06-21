def g(x):
    ret = 1 if x % 4 in {1, 2} else 0
    for i in range(1, 50):
        if x % (2 << i) >= (1 << i) and not x % 2:
            ret += (1 << i)
    return ret


A, B = map(int, input().split())
print(g(A - 1) ^ g(B))
