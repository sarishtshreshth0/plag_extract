power = [2,3,4,5,6,7,8,9,10,11,12,13,1,]
A,B = map(int, input().split())
if power.index(A) > power.index(B):
    print("Alice")
elif A == B:
    print("Draw")
else:
    print("Bob")
