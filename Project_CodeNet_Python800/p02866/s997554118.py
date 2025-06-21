n = int(input())
d = list(map(int, input().split()))

e = [0 for i in range(n)]

if d[0] != 0:
    print(0)
    exit()

for i in d:
    e[i] += 1

# print(e)

ans = 1

for i in range(1, n):
    ans *= e[d[i] - 1]
    ans %= 998244353
print(ans)
