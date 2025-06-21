
[A,B] = list(map(int,input().split()))

flag=0
for C in range(1,4):
    if A*B*C %2 ==1:
        flag=1
        break

if flag==1:
    print('Yes')
else:
    print('No')