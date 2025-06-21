from sys import exit

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

m,d = mi()

ans=0

for i in range(1,m+1):
    for j in range(1,d+1):
        if j<22:
            continue

        d1 = j%10
        d10 = j//10
        if d1>=2 and d10>=2 and d1*d10 == i:
            ans += 1
print(ans)
