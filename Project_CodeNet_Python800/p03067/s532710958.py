A = [int(x) for x in input().split()]
a = list(sorted(A))
print("Yes" if A[2] == a[1] else "No")