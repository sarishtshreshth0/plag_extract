A, B, C = map(int, input().split())
if (C < min(A, B)) or (max(A, B) < C):
    print("No")
else:
    print("Yes")
