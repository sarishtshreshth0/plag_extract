n = str(input())
num = 0
for i in n:
    num += int(i)
if int(n)%num == 0:
    print('Yes')
else:
    print('No')