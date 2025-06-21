ipt = list(map(int, input().split()))
if min(ipt[0], ipt[1]) < ipt[2] < max(ipt[0], ipt[1]):
    print("Yes")
else:
    print("No")