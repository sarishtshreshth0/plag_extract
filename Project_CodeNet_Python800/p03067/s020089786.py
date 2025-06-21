li = list(map(int, input().split()))
print("Yes" if sorted(li).index(li[2]) == 1 else "No")