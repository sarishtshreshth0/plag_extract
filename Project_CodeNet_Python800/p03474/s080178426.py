a,b = map(int,input().split())
s = str(input())
#suji = [str(i) for i in range(10)]
ans = True
for i in range(a+b+1):
    if i==a:
        if s[i]!='-':
            ans = False
    else:
        if s[i]=='-':
            ans = False
if ans:
    print('Yes')
else:
    print('No')