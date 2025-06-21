As=list(map(int,input().split()))

for A in range(2):
    if As[A]==1:
        As[A]+=13
        
if As[0]==As[1]:
    print("Draw")
elif As[0]>As[1]:
    print("Alice")
else:
    print("Bob")