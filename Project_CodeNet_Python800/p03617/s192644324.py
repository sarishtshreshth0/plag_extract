T = list(map(int,input().split()))
n = int(input())*4
q_s = 1
h_s = 2
s_s = 4
d_s = 8

L = []
temp = 1
for i in range(4):
    s = temp
    v = T[i] / s
    L.append([T[i],s,v])
    temp *= 2

L.sort(key=lambda x: x[2])

ans = 0
for l in L:
    ans += (n // l[1])*l[0]
    n = n % l[1]

print(ans)