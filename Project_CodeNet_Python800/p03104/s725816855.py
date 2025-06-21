def f(n):
    num=n%4
    if num==0:return n
    elif num==1:return 1
    elif num==2:return n+1
    else:return 0


a,b=map(int,input().split())
print(f(a-1)^f(b))