x,y,z=(map(int,input().split()))
if(y<x):
    x,y=y,x
if(z>=x and z<=y):
    print("Yes")
else:
    print('No')
