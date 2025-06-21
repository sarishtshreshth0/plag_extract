x,y=map(int,input().split())
s=input()
d=s.count('-')
if('-' in s):
    f=s.index('-')
if(d==1 and f==x):
    print("Yes")
else:
    print("No")
