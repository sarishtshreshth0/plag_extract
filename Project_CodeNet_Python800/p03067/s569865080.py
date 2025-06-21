def inpl():
    return list(map(int, input().split()))


A, B, C = inpl()
A, B = min(A, B), max(A, B)
print('Yes' if A <= C <= B else 'No')