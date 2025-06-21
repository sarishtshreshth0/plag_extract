from operator import itemgetter

n = int(input())
r = [tuple(map(int, input().split())) for i in range(n)]
b = [tuple(map(int, input().split())) for i in range(n)]

r = sorted(r, key=itemgetter(1), reverse=True)
b.sort()

pair = [False]*n

for i in range(n):
    for j in range(n):
        if b[i][0] > r[j][0] and b[i][1] > r[j][1] and pair[j] == False:
            pair[j] = True
            break

print(sum(pair))