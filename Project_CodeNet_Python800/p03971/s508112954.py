N,A,B=map(int,input().split())
S=input()
S=list(S)
count=0
world=1
for i in S:
    if i=="a":
        if count<A+B:
            print("Yes")
            count+=1
        else:
            print("No")
    elif i=="b":
        if (count<A+B) & (world<=B):
            print("Yes")
            count+=1
            world+=1
        else:
            print("No")
    else:
        print("No")