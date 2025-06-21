n=int(input())

def findsum0fdigit(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum
        
if n%findsum0fdigit(n)==0:
    print("Yes")
else:
    print("No")