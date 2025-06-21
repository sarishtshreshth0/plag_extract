def divisor(n):
    tank = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            tank.append((i, n//i))
    return tank

m,d = map(int,input().split())
cnt = 0
for i in range(1,m+1):
    k = divisor(i)
    for x,y in k:
        a = int(str(x)+str(y))
        if a//10>=2 and a%10>=2 and a<=d:
            cnt += 1
        if x!=y:
            b = int(str(y)+str(x))    
            if b//10>=2 and b%10>=2 and b<=d:
                cnt += 1
print(cnt)