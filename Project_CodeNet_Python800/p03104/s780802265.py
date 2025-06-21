a, b = list(map(int, input().split()))

def xor_sum(n):
    if n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n+1
    elif n % 4 == 3:
        return 0
    else:
        return n

if a == 0:
    print(xor_sum(b))
else:
    print(xor_sum(a-1) ^ xor_sum(b))