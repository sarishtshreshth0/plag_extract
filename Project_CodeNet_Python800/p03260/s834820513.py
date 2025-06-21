def yn(P):
    if P:
        print("Yes")
    else:
        print("No")

a,b=map(int,input().split())
yn(a%2!=0 and b%2!=0)