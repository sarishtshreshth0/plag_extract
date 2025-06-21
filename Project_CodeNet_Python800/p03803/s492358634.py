strength=[2,3,4,5,6,7,8,9,10,11,12,13,1]
A,B=map(int,input().split())
a=strength.index(A)
b=strength.index(B)
if a>b:
    print("Alice")
elif b>a:
    print("Bob")
elif a==b:
    print("Draw")