N,A,B=map(int, input().split())
S=input()
count=0
astu=0
for s in S:
    if s=="a":
        if count<A+B:
            print("Yes")
            count+=1
        else:
            print("No")
    elif s=="b":
        if count<A+B and astu<B:
            print("Yes")
            astu+=1
            count+=1
        else:
            print("No")
    else:
        print("No")