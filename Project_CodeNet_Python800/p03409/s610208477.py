from heapq import heapify, heappop, heappush
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(n)]
A = [[x, y, 0] for x, y in ab]
B = [[x, y, 1] for x, y in cd]
abcd = A+B
abcd.sort()

a = []
heapify(a)
result = 0
for i in range(2*n):
    x, y, h = abcd[i]
    if h==0:
        heappush(a, -y)
    else:
        if len(a) > 0:
            a_y = heappop(a)
            h = []
            while y+a_y < 0:
                h.append(a_y)
                if len(a) > 0:
                    a_y = heappop(a)
                else:
                    break
            if y+a_y>0:
                result += 1
            for j in h:
                heappush(a, j)
        
print(result)