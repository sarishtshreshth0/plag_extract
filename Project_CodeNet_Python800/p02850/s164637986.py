import sys
input = sys.stdin.readline

n = int(input())
l=[[]]
nn = []
for _ in range(n+1):
    l.append([])

for i in range(n-1):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)
    nn.append(b)

ml = list(map(len,l)) 
m = max(ml)
co = []
for i in range(n+1):
    co.append( set(range(1,ml[i]+1) ))

col = [0]*(n+1)
col[1] = 1

for i in range(1,n+1):
    for la in l[i]:
        if col[la] ==0:
            col[la] = co[i].pop()
            co[la].discard(col[la])
print(m)
for i in range(n-1):
    print(col[nn[i]])
