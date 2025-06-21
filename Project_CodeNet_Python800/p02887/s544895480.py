# 問題：https://atcoder.jp/contests/abc143/tasks/abc143_c

n = int(input())
slimes = input()
res = 1
for i in range(1, n):
    if slimes[i-1] != slimes[i]:
        res += 1
print(res)
