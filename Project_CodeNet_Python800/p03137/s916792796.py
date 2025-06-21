n,m = map(int,input().split())
x = list(map(int,input().split()))
t_3 = max(x) - min(x)
t = []
t_2 = 0
x.sort()
if m == 1:
    print(0)
    exit()

for i in range(m-1):
    t.append(x[i+1]-x[i])

t.sort(reverse=True)
pp = min(n-1,m-1)
for i in range(pp):
    t_2 += t[i]

print(t_3-t_2)
