N, M = map(int, input().split())
ans = [-1] * N

def find(x):
    global ans
    if ans[x] == -1:
        return x
    else:
        ans[x] = find(ans[x])
        return ans[x]
    
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    xx = find(x)
    yy = find(y)
    if ans[x] == ans[y] == -1:
        ans[y] = x
    elif xx == yy:
        continue
    else:
        ans[yy] = xx

n = 0
for i in ans:
    if i == -1:
        n += 1

print(n)