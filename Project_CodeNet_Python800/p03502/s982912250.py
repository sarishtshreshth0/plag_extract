n = input()
print("Yes" if int(n) % sum([int(x) for x in n]) == 0 else "No")