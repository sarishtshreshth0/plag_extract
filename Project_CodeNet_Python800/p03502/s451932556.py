n=int(input())
a=0
m=n
if n==0:
    print("No")

else:
    
    while n>0:
        
        a=a+n%10
        n=n//10
    if m%a==0:
        print("Yes")
    else:
        print("No")
    
