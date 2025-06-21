a = [int(item) for item in input().split()]
print("No" if a[2] in (max(a), min(a)) else "Yes")