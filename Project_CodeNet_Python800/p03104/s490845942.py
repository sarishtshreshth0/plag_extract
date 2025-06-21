
A, B = map(int, input().split())

# 0 ^ 1 ^ ... ^ N
def xor_0_to_N(N):
    if (N+1) % 2 == 0:
        s = (N+1) // 2 % 2
    else:
        s = ((N+1) // 2 % 2) ^ N
    return s

"""
XOR = 0
for i in range(1, 20):
    print("idx", i)
    XOR ^= i
    print(XOR)
    print(xor_0_to_N(i))
"""

print(xor_0_to_N(A-1) ^ xor_0_to_N(B))