A,B=map(int, input().split())
if A==1 and not(A==B):
    print("Alice")
elif B==1 and not(A==B):
    print("Bob")
else:
    if A>B:
        print('Alice')
    elif A==B:
        print('Draw')
    else:
        print('Bob')
