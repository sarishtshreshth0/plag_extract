N = int(input())
R = []
B = []
R_tmp = []
for _ in range(N):
    a,b = map(int,input().split())
    R_tmp.append(a)
    R.append([a,b])

for _ in range(N):
    a,b = map(int,input().split())
    B.append([a,b])

B = sorted(B)
R = sorted(R)
R_tmp.sort()
from bisect import bisect_left
ans = 0
for x in B:
    index = bisect_left(R_tmp,x[0])
    tmp = R[:index]
    tmp = sorted(tmp,key=lambda x:x[1])
    for i in range(index)[::-1]:
        if tmp[i][1] < x[1]:
            R.remove([tmp[i][0],tmp[i][1]])
            R_tmp.remove(tmp[i][0])
            ans += 1
            break
print(ans)

