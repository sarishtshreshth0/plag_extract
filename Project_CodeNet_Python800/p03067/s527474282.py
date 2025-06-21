a,b,c=map(int,input().split())
if a > c > b:
    print("Yes")
else:
    if b > c > a:
        print("Yes")
    else:
        print("No")