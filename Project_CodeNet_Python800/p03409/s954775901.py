n=int(input())
r = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

from operator import itemgetter
r = sorted(r, key=itemgetter(1),reverse=1)
b = sorted(b)

x=0
y=[200,200]
z=[0,0]

for i in range(n):
    for j in range(n):
        if b[i][0] > r[j][0] and b[i][1] > r[j][1]:
            x+=1
            r[j] = y
            b[i] = z
            break

print(x)