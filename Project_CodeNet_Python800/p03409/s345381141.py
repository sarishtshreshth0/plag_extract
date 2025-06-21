N = int(input())
R = [list(map(int,input().split())) for i in range(N) ]
B = [list(map(int,input().split()))  for i in range(N) ]
R.sort(key=lambda x:x[1],reverse=1)
B.sort()
ans = 0
for b in B:
    for r in R:
        if b[1]>r[1] and b[0]>r[0]:
            ans += 1
            R.remove(r)
            break
print(ans)
