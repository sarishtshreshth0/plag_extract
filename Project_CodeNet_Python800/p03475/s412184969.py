import sys
input = sys.stdin.readline
n = int(input())
c, s, f = [0]*(n-1), [0]*(n-1), [0]*(n-1)
for i in range(n-1):
    c[i], s[i], f[i] = map(int, input().split())

ans = [0]*n
for i in range(n-1):
    time = s[i]
    for j in range(i, n-1):
        if time < s[j]:
            time = s[j]
        if time % f[j] != 0:
            time += f[j] - time % f[j]
        time += c[j]
    ans[i] = time

for i in ans:
    print(i)