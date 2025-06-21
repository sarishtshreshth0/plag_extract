A,B,C=map(int,input().split())
if A<B:
    while True:
        if A==C:
            print("Yes")
            break
        if A==B:
            print("No")
            break
        A+=1
if B<A:
    while True:
        if A==C:
            print("Yes")
            break
        if A==B:
            print("No")
            break
        A-=1