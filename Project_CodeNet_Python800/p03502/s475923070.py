n = int(input())
nl = str(n)
d = 0
for i in nl:
    d += int(i)

print("Yes") if n % d == 0 else print("No")