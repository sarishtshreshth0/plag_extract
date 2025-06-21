import heapq

n, m = map(int, input().split())
dic = {}
for i in range(n):
    ai, bi = map(int, input().split())
    if ai in dic:
        dic[ai].append(bi)
    else:
        dic[ai] = [bi]

for key in dic.keys():
    dic[key] = sorted(dic[key])

ans = 0
hp = []
heapq.heapify(hp)
for i in range(1, m+1):
    if i in dic:
        heapq.heappush(hp, (-dic[i].pop(), i))
    if hp != []:
        maxi = heapq.heappop(hp)
        ans += -maxi[0]
        if dic[maxi[1]] != []:
            heapq.heappush(hp, (-dic[maxi[1]].pop(), maxi[1]))
print(ans)