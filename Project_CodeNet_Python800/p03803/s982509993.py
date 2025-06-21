a,b=map(int, input().split())
if a==b:
    print('Draw')
elif a==13 and b==1:
    print('Bob')
elif a==1 and b==13:
    print('Alice')
else:
    print(['Alice','Bob'][a<b])