a,b,c = map(int,input().split())

if (a<c and c<b) or (c<a and b<c):
    print('Yes')
else:
    print('No')
