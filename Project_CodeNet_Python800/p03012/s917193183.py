n = int(input())
w = list(map(int,input().split()))
s = sum(w)

c = 0
prev_d = float('inf')
for x in w:
    c += x
    dis = abs((s - c) - c)
    if c >= s / 2:
        print(min(dis,prev_d))
        exit()
    prev_d = dis

