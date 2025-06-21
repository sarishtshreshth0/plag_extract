import heapq
n,m = map(int,input().split())
ma = {}
for _ in range(n):
    a,b = map(int,input().split())
    start = a
    if start<0:
        continue
    if start in ma:
        ma[start].append(-b)
    else:
        ma[start] = [-b]
li = []
heapq.heapify(li)
ans_li = []
#print(li,ma)
for i in range(m):
    if i+1 in ma:
        for m in ma[i+1]:
            heapq.heappush(li, m)
    if len(li)>0:
        tmp = heapq.heappop(li)
        ans_li.append(-tmp)
        #print(tmp)
print(sum(ans_li))