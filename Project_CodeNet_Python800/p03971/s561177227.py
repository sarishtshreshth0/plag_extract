N,A,B = map(int,input().split())
S = input()

FOR = 1
CNT = 0
for i,s in enumerate(list(S)):
    if s=="a" and CNT < A+B:
        print("Yes")
        CNT+=1
    elif s=="b" and CNT < A+B and FOR <=B:
        print("Yes")
        CNT+=1
        FOR+=1
    else:
        print("No")