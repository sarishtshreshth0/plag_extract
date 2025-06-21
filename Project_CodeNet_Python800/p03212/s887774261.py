import sys
n=int(input())

def f(x):
    m=0
    while x>0:
        m+=1
        x=x//10
    return m
m=f(n)

a=[(3**(i+1)-3)//2-6*(2**i-1)+3*i for i in range(1,10)]
a.insert(0,0)
if m==1 or m==2:
    print(0)
    sys.exit()
ans=a[m-1]
def g(x):
    z=[]
    while x>0:
        z.insert(0,x%10)
        x=x//10
    return z
for i in range(3**m):
    x=["" for i in range(m)]
    for j in range(m):
        if i%3==0:
            x[j]="3"
        elif i%3==1:
            x[j]="5"
        else:
            x[j]="7"
        i=i//3
    if int("".join(x))<=n and "3" in x and "5" in x and "7" in x:
        ans+=1
    
print(ans)
        
    
    



    
        
        
        
          
