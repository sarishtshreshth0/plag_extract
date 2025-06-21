a,b=map(int,input().split())
if a==b:
    print("Draw")
elif 1<a<b or b==1:
    print("Bob")
else:
    print("Alice")
