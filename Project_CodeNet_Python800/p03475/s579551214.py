n = int(input())
loss = []

for _ in range(n-1):
    c,s,f = map(int,input().split())
    loss.append((c,s,f))

for i in range(n-1):
    time = 0
    for j in range(i,n-1):
        if time < loss[j][1]:
            time = loss[j][1]
        if (time-loss[j][1])%loss[j][2] != 0:
            time += loss[j][2]-(time-loss[j][1])%loss[j][2]
        time += loss[j][0]
    print(time)
print(0)