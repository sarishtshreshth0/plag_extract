N = int(input())
red = [tuple(map(int,input().split())) for _ in range(N)]
blue = [tuple(map(int,input().split())) for _ in range(N)]
 
red.sort(key=lambda x:x[0], reverse=True)
blue.sort(key=lambda x:x[1])
 
ans = 0
for i in range(N):
    a,b = red[i]
    for j in range(len(blue)):
        c,d = blue[j]
        if a < c and b < d:
            blue.pop(j)
            ans += 1
            break
print(ans)
