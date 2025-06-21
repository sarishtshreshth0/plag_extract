n = int(input())

i = 1
ans = 0
while i * i <= n:
    if n % i == 0:
        ans = max(len(str(i)), len(str(n // i)))
    i += 1
print(ans)