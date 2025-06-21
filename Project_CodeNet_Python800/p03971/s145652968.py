N,A,B=map(int,input().split())
S=list(input())

p=0
q=0

for i in S:
    if p<A+B and i=="a":
        print("Yes")
        p+=1
    
    elif p<A+B and  i=="b" and q+1<=B:
        print("Yes")
        p+=1
        q+=1
    else:
        print("No")