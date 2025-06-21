a,b = map(int,input().split())
l = []
if a % 4 != 0:
    for i in range(a-1,-6,-1):
        l.append(i)
        if i % 4 == 0:
            break
if b % 4 != 3:
    for i in range(b+1,10**12+5):
        l.append(i)
        if i % 4 == 3:
            break
# print(l)
ans = 0
for i in l:
    ans = ans ^ i
print(ans)