# coding: utf-8

a,b,c,d=list(map(int,input().split()))

if a<=c<b<d:
    print(b-c)
elif a<c<d<=b:
    print(d-c)
elif c<=a<d<b:
    print(d-a)
elif c<a<b<=d:
    print(b-a)
elif a==c<b==d:
    print(b-a)
else:
    print(0)