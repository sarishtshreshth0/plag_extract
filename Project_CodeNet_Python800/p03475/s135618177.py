N = int(input())
Plan = [list(map(int,input().split())) for _ in range(N-1)]

for i in range(N-1):
    c1,s1,f1 = Plan[i]
    time = s1+c1
    for j in range(i+1,N-1):
        c,s,f = Plan[j]
        if time <= s:
            time = s
        elif (time-s)%f != 0:
            time += f-(time-s)%f
        time += c
    print(time)
print(0)