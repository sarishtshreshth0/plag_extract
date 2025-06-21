n = int(input())
print("Yes" if n % sum([int(q) for q in str(n)]) == 0 else "No")