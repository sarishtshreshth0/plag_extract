A, B, C, D = map(int, input().split())
a = set(range(A, B))
b = set(range(C, D))
c = a& b

print(len(c))