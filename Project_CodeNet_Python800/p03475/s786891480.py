N = int(input())
dia = []
for _ in range(N-1):
    c,s,f = map(int,input().split())
    dia.append((c,s,f))
for i in range(N-1):
    time = 0
    for j in range(i,N-1):
        c,s,f = dia[j]
        while time > s:
            s += f

        time = s + c
    print(time)
print(0)








