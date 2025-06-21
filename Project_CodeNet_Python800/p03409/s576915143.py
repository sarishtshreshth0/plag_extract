N = int(input())
red = []
blue = []
for i in range(N):
    in1, in2 = list(map(int,input().split()))
    red.append([in1, in2])
for i in range(N):
    in1, in2 = list(map(int,input().split()))
    blue.append([in1, in2])
    
red = sorted(red, key=lambda x: x[0])[::-1]
ans = 0
INF = 10 ** 9 + 7
for i in range(N):
    min_ = INF
    ind = -1
    for j in range(N):
        if red[i][0] <= blue[j][0] and red[i][1] <= blue[j][1] and blue[j][1] < min_:
            ind = j
            min_ = blue[j][1]
    if ind != -1:
        blue[ind][0] = -1
        ans += 1
print(ans)