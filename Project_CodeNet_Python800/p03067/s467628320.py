m = list(map(int,input().split()))

if m[0]<m[2]<m[1]:
    print('Yes')
elif m[1]<m[2]<m[0]:
    print('Yes')
else:
    print('No')