A, B, C = map(int, input().split())
if A > B:
    A, B = B, A
print("Yes") if A < C < B else print("No")
