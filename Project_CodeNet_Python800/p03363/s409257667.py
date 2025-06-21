n = int(input())
a = list(map(int, input().split()))

acc = [0 for i in range(n+1)]
for i in range(n):
    acc[i+1] = a[i] + acc[i]

ans = {}
for x in acc:
    ans.setdefault(x, 0)
    ans[x] += 1
cnt = 0
for i in ans:
    cnt += ans[i]*(ans[i]-1)//2

print(cnt)