a = list(map(int,input().split()))
if min(a) != a[2] and max(a) != a[2]:
    print("Yes")
else:
    print("No")