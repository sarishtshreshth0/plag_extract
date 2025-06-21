X=int(input())
a=X//500
if X%500==0:
    print(a*1000)
else:
    b=(X-500*a)//5
    print(a*1000+b*5)