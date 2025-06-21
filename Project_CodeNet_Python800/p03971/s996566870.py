N,A,B=map(int,input().split())
S=input()
count=0
out=1
for s in S:
    if s=="a" and count<A+B:
        count+=1
        print("Yes")
    elif s=="b" and count<A+B and out<=B:
        count+=1
        out+=1
        print("Yes")
    else:
        print("No")