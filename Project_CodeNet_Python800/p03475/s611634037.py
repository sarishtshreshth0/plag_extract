N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N-1)]

for i in range(N):
    ans = 0
    for j in range(i, N-1):
        if j == i:
            ans += CSF[i][1]
            ans += CSF[i][0]
        else:
            if ans < CSF[j][1]:
                ans += CSF[j][1] - ans
            else:
                mod = (ans - CSF[j][1]) % CSF[j][2]
                if mod != 0:
                    ans += CSF[j][2] - mod
            ans += CSF[j][0]
    print(ans)