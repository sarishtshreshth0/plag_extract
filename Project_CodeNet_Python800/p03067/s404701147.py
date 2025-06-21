a, b, c = map(int, input().split())
print('Yes') if (a < c < b) | (b < c <a) else print('No')