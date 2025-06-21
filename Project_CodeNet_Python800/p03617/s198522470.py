A = list(map(int,input().split()))
n = int(input())
base = {}
for i in range(4):
    tmp = 2**(i)
    base.update({i:A[i]/tmp})
dict = sorted(base.items(), key=lambda x: x[1])
m = n*4
ans = 0
for x in dict:
    y = 2**(x[0])
    kosuu = m // y
    m -= y*kosuu
    ans += kosuu*A[x[0]]
print(ans)
