from operator import itemgetter

n = int(input())
red = [list(map(int, input().split())) for i in range(n)]
blue = [list(map(int, input().split())) for i in range(n)]

red.sort()
blue.sort(key=itemgetter(1))

ans = 0
for i in range(n):
    a,b = red[-i-1]
    for j in range(len(blue)):
        c,d = blue[j]
        if a<c and b<d:
            ans += 1
            blue[j]=[0,0]
            break
print(ans)