a, b = [int(w) for w in input().split()]
cond = a*b % 2 == 1
print("Yes" if cond else "No")
