n,d = map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]
l = []
o = []

for i in range(n):
    for j in range(i+1,n):
        t = 0
        for k in range(d):
            t += abs(x[i][k] - x[j][k]) ** 2
        l.append(t)

l.sort()
i = 1
while i ** 2 <= l[-1]:
    o.append(i ** 2)
    i += 1

p = 0
for i in range(len(o)):
    p += l.count(o[i])

print(p)