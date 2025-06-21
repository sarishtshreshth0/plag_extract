a, b = map(int, input().split())
a = a if a > 1 else 14
b = b if b > 1 else 14
print("Alice" if a > b else "Bob" if a < b else "Draw")