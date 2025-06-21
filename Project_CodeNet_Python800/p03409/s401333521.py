N = int(input())

R = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
R.sort(key=lambda x:(-x[0],-x[1]))
B.sort(key=lambda x:(x[1],x[0]))

ans = 0
for rx,ry in R:
    for bx,by in B:
        # print(rx,ry,bx,by)
        if rx<bx and ry<by:
            # print("ok")
            ans += 1
            B.remove([bx,by])
            break

print(ans)