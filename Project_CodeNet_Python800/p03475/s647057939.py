n = int(input())
csf = [list(map(int,input().split())) for i in range(n-1)]
t = [[0] * n for i in range(n)]
for i in range(n-1):
    cc, cs, cf = csf[i][0], csf[i][1], csf[i][2]
    t[i][i] = cs
    for j in range(1+i):
        cs = csf[i][1]
        while t[j][i] > cs:
            cs += cf
        t[j][i+1] = cs + cc 
for i in range(n):
    print(t[i][n-1])