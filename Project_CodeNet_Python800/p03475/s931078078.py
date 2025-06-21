N = int(input())
dia = [0]*(N-1)
for i in range(N-1):
    c,s,f = map(int,input().split())
    dia[i] = (c,s,f)
for i in range(N-1):
    time = 0
    for j in range(i,N-1):
        c,s,f = dia[j]
        if time > s:
            x = (time - s)/f
            if x.is_integer():
                s += int(x)*f
            else:
                s += int(x+1)*f
        time =  s + c
    print(time)
print(0)








