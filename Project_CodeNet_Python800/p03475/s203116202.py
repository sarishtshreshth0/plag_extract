N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N-1)]

ans = 0
memo = {}
memoset = set()
def dfs(i, time):
    if i==N-1:
        return time
    c, s, f = CSF[i]
    if time<s:
        time = s
    elif time%f!=0:
        time = (time//f+1)*f
    if (time, i) in memoset:
        return memo[(time, i)]
    T = dfs(i+1, time+c)
    memo[(time, i)] = T
    memoset.add((time, i))
    return T

for i in range(N-1):
    print(dfs(i, 0))
print(0)