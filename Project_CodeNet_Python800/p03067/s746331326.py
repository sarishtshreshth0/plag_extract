a, b, c = map(int, input().split())

print('Yes' if c != max(a, b, c) and c != min(a, b, c) else 'No')