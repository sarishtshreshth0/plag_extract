N,A,B=map(int,input().split())
S=input()

passer=0
passb=0
for p in S:
    if p =="c":
        print("No")
    if p=="a":
        if passer < A+B:
            print("Yes")
            passer+=1
        else:
            print("No")
    if p=="b":
        if passer <A+B and passb <B:
            print("Yes")
            passer+=1
            passb+=1
        else:
            print("No")