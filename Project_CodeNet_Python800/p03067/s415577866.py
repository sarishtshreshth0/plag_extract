a, b, c = map(int, input().split())
A = min(a, b)
B = max(a, b)


if c in range(A, B + 1):
    print("Yes")
else:
    print("No")
