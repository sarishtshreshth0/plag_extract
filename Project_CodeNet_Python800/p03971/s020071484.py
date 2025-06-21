N,A,B=map(int,input().split())
S=input()
cnt1,cnt2=0,0
for i,s in enumerate(S):
    if s=="c":
        print("No")
        continue
    if s=="a":
        if cnt1<A+B:
            print("Yes")
            cnt1+=1
        else:
            print("No")
    else:
        if cnt1<A+B and cnt2<B:
            print("Yes")
            cnt1+=1
            cnt2+=1
        else:
            print("No")