a, b = (int(_) for _ in input().split())

def xor(n):
    m = 0
    if (n % 4 == 0):
        m = n
    elif (n % 4 == 1):
        m = 1
    elif (n % 4 == 2):
        m = n + 1
    return (m)

A = xor(a - 1)
B = xor(b)
print(A ^ B)
