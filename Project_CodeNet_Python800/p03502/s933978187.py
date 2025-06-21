n = list(input())
print("Yes" if int("".join(n)) % sum(map(int, n))== 0 else "No")