a,b=map(int,input().split())
s=[2,3,4,5,6,7,8,9,10,11,12,13,1]
a=s.index(a)
b=s.index(b)
if a>b:
    print("Alice")
elif a<b:
    print("Bob")
else:
    print("Draw")
