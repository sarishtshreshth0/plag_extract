from heapq import heappush, heappop
n,m = map(int,input().split())
work_dict = {}
for i in range(n):
    a,b = map(int,input().split())
    if not a in work_dict.keys():
        work_dict[a] = []
    work_dict[a].append(b)
hq = []
ans = 0
for i in range(1,m+1):
    if i in work_dict.keys():
        for j in range(len(work_dict[i])):
            heappush(hq, -work_dict[i][j])
    if len(hq) > 0:
        work = heappop(hq)
        ans += -work
print(ans)