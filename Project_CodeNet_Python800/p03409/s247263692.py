N = int(input())
R = []
B = []
for _ in range(N):
    R.append(list(map(int,input().split())))
for _ in range(N):
    B.append(list(map(int,input().split())))
B.sort()
flag = [1 for i in range(N)]
ans = 0
for i in range(N):
    MAX = -1
    index = -1
    for j in range(N):
        if flag[j] and R[j][0] < B[i][0] and R[j][1] < B[i][1] and MAX < R[j][1]:
            MAX = R[j][1]
            index = j
    if index == -1:
        continue
    flag[index] = 0
    ans += 1
print(ans)