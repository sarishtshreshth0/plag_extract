n,m = map(int,input().split())



def fun():
    if int(m/2) == m/2:
        ans = n*m/2
    else:
        if int(n/2)==n/2:
            ans = n*m/2
        else:
            ans = (n*m/2)+0.5
    
    print(int(ans))  
    
if n == 1 or m ==1:
    print("1")
else:
    fun()