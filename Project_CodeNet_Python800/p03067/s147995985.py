A, B, C = map(int, input().split())
if min(A, B) <= C and C <= max(A, B):
    print("Yes")
else:
    print("No")