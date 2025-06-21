def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

m,d = iim()
ans = 0
for i in range(1,m+1):
    for j in range(1,d+1):
#        print('{}/{}'.format(i,j))
        d10 = j//10
        d1 = j-d10*10
        if d10 > 1 and d1 > 1 and i == d10*d1:
            ans += 1
print(ans)