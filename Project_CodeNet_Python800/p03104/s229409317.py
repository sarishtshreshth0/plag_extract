a, b = [int(x) for x in input().split()]

def f_xor(n):
    temp = (n // 2) % 2
    if n % 2 == 0:
        temp ^= n
    else:
        temp ^= 1
    return temp

if a == 0:
    print(f_xor(b))
else:
    print(f_xor(a - 1) ^ f_xor(b))