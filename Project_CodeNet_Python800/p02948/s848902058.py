import heapq

n, m = list(map(int, input().split()))

ab = []

for i in range(n):
    a, b = list(map(int, input().split()))
    ab.append([a, b])

ab.sort()

d = 1

w = []
heapq.heapify(w)

p = 0
d = 1
i = 0
while d <= m:
    while i < n and ab[i][0] == d:
        a, b = ab[i]
        heapq.heappush(w, -b)
        i += 1
    #print(w)
        #d日前にやる仕事をきめる
    if len(w) > 0:
        p -= heapq.heappop(w)

    d += 1


print(p)
