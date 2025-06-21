import sys
input = sys.stdin.readline
N = int(input())
red = [list(map(int,input().split())) for i in range(N)]
blue = [list(map(int,input().split())) for i in range(N)]

red.sort(key=lambda x : -x[1])
blue.sort()

ans = 0
red_used = [0 for _ in range(N)]
for b in blue :
    for i in range(N) :
        if b[0] > red[i][0] and b[1] > red[i][1] :
            if red_used[i] == 0 :
                ans += 1
                red_used[i] = 1
                break

print(ans)
