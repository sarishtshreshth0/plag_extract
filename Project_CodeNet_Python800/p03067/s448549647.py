A, B, C = map(int, input().split())
print('Yes' if C in range(min(A, B)+1, max(A, B)) else 'No')