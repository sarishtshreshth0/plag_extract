n = int(input())

ans = 11
for i in range(1, int(n ** (1/2)) + 1):
    if n % i == 0:
        ans = min(ans, max(map(lambda x: len(str(x)), [i, n//i])))
print(ans)
