
a,b,c=map(int,input().split())
if c-a > 0 and c-b < 0:
    print('Yes')
elif c-a < 0 and c-b > 0:
    print('Yes')
else:
    print('No')