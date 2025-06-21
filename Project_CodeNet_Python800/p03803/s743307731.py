x,y=map(int,input().split())
if x==y:
    print('Draw')
elif x<y and x==1:
    print('Alice')
elif x>y and y==1:
    print('Bob')
else:
    print('Alice' if x>y else 'Bob') 