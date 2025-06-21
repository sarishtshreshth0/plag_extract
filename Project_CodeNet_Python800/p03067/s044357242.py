A, B, C = tuple(map(int, input().split()))
if A < C < B or B < C < A:
    print("Yes")
else:
    print("No")