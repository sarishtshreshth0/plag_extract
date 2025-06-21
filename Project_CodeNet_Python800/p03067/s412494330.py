A, B, C = map(int, input().split())

print('Yes' if min(A,B) < C and C < max(A,B) else 'No')