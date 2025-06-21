n = int(input())
ai = [int(i) for i in input().split()]

s = [0]
tmp = 0

for i in range(n):
    tmp += ai[i]
    s.append(tmp)
    
#print(s)
s.sort()

tmp = s[0]
ans = 0
num = 1
#print(s)

for i in range(1,n+1):
    if s[i] == tmp:
        num += 1
    else:
        #print(num,ans)
        ans += num*(num-1)//2
        tmp = s[i]
        num = 1

ans += num*(num-1)//2

print(ans)