a,b=map(int,input().split())
if a%2==0:
    if b%2==0:
        use=((b-a)//2)%2
        print(use^b) 
    else:
        use=((b-a+1)//2)%2
        print(use)
else:
    temp=a 
    a+=1
    if b%2==0:
        use=((b-a)//2)%2
        print(temp^use^b) 
    else:
        use=((b-a+1)//2)%2
        print(temp^use)   