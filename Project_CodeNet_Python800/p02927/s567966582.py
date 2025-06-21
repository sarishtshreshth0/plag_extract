m,d = map(int,input().split())
ans = 0
for M in range(1,m+1):
    for D in range(1,d+1):
        D = '0' + str(D)
        if int(D[-1]) * int(D[-2]) == M and int(D[-2]) >= 2 and int(D[-1]) >= 2:
            ans-=-1


print(ans)