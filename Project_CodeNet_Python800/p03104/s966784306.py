a,b=map(int,input().split())

if a==b:
    print(a)
elif a%2==0 and b%2==1:
    if ((b+1-a)//2)%2==0:
        print(0)
    else:
        print(1)
elif a%2==1 and b%2==1:
    if ((b-a)//2)%2==0:
        print(0^a)
    else:
        print(1^a)
elif a%2==0 and b%2==0:
    if ((b-a)//2)%2==0:
        print(0^b)
    else:
        print(1^b)
elif a%2==1 and b%2==0:
    if ((b-a-1)//2)%2==0:
        print(a^0^b)
    else:
        print(a^1^b)

