n, m = map(int,input().split())
li = list(map(int,input().split()))
ans = []

if n >= m:
    print(0)
    exit()

li.sort()

for i in range(m-1):
    ans.append(li[i+1]-li[i])

ans.sort(reverse=True)
print(sum(ans[n-1:]))