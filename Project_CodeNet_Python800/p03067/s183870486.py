a, b, c = [int(_) for _ in input().split()]
print('Yes' if min(a, b) < c < max(a, b) else 'No')