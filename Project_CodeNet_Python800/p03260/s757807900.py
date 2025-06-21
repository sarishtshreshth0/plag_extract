a, b = [int(i) for i in input().split()]

print("Yes" if any((a * b * i) % 2 == 1 for i in [1, 2, 3]) else "No")
