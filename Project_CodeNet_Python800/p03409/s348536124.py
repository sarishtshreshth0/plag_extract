N = int(input())
red = [tuple(map(int, input().split())) for _ in range(N)]
blue = [tuple(map(int, input().split())) for _ in range(N)]

from operator import itemgetter
red = sorted(red, reverse=True)
blue = sorted(blue, key=itemgetter(1))

seen = [0] * N
ans = 0
for i in range(N):
    for j in range(N):
        if seen[j] == 0 and red[i][0] < blue[j][0] and red[i][1] < blue[j][1]:
            seen[j] = 1
            ans += 1
            break

print(ans)