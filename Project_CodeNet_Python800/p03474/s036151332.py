a,b = map(int,input().split())
s = list(input())
if s[a] != '-':
    print('No')
    exit()
s[a]='0'
for i in s:
    if i not in [str(j) for j in range(0,10)]:
        print('No')
        exit()
print('Yes')