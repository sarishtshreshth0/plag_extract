A, B = map(int, input().split())
A = A if A != 1 else 14
B = B if B != 1 else 14
print("Draw" if A == B else "Alice" if A > B else "Bob")