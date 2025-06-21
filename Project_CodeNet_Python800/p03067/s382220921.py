A, B, C = [int(x) for x in input().split()]

if max(A, B) > C and min(A, B) < C:
    print("Yes")
else:
    print("No")