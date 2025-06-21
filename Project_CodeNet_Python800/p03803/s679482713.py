a = list(map(int, input().split()))
print("Draw" if a[0] == a[1] else ("Alice" if a[0] > a[1] and a[1] != 1 or a[0] == 1 else "Bob"))