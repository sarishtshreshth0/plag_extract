import math
n = int(input())
st = [list(map(int, input().split())) for i in range(n-1)]
for j in range(n-1):
    t = st[j][1]+st[j][0]
    for i in range(j+1,n-1):
        if t<st[i][1]:
            t = st[i][1]
        elif (t-st[i][1])%st[i][2]!=0:
            t += st[i][2]-(t-st[i][1])%st[i][2]
        t += st[i][0]
    print(t)
print(0)