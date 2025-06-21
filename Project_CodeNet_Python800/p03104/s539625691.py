n, m = map(int, input().split())

def cumXOR(k):
    if k % 4 == 0:
        return k
    elif k % 4 == 1:
        return 1
    elif k % 4 == 2:
        return k + 1
    else:
        return 0

print(cumXOR(n-1)^cumXOR(m))
