n = int(input())
c = [0]*(n-1)
for i in range(n-1):
    c[i] = list(map(int,input().split()))
for i in range(n-1):
    t = c[i][1]
    for j in range(i,n-1):
        if t <= c[j][1]:
            t = c[j][1]
            t += c[j][0]
        else:
            t +=  -(-t//c[j][2])*c[j][2] - t + c[j][0]
    print(t)
print(0)