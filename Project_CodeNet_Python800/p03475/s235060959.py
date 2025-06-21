n = int(input())
C = []
S = []
F = []
for i in range(n-1):
    c,s,f = map(int,input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for start in range(n-1):
    time = S[start]
    for i in range(start,n-1):
        time += C[i]
        if i != n-2:
            if time <= S[i+1]:
                time = S[i+1]
            elif time%F[i+1] != 0:
                time += F[i+1]-time%F[i+1]
    print(time)
print(0)