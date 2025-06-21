A, B, C = list(map(int, input().split()))
if A > B:
    if A > C > B:
        print("Yes")
    else:
        print("No")
else:
    if B > C > A:
        print("Yes")
    else:
        print("No")