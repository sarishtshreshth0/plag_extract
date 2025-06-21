a, b = map(int, input().split())
s = input()
cnt = 0
y = ['0','1','2','3','4','5','6','7','8','9']

for i in range(a+b+1):
    if i == a:
        if s[a] == '-':
            cnt +=1
    else:
        if s[i] in y:
            cnt += 1
        
if cnt == (a+b+1):
    print('Yes')
else:
    print('No')