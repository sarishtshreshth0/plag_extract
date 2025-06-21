n = int(input())
w = [input() for _ in range(n)]

ans = 'Yes'
for i in range(1, n):
    if (w[i] in w[:i]) or (w[i][0] != w[i - 1][-1]):
        ans = 'No'
        break
print(ans)
