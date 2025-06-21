import sys
A, B = map(int, input().split())
flag = 0
for i in range(1,3):
    if ((A*B*i)%2)!=0:
        print('Yes')
        flag=1
        sys.exit()

if flag!=1:
    print('No')