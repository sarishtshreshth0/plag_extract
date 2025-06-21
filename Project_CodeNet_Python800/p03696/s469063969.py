N=int(input())
S=input()

left=0
cnt1=0
cnt2=0

for i in range(N):
    if S[i]=="(":
        cnt1+=1
    elif S[i]==")":
        cnt2+=1
        if i<N-2 and S[i+1]=="(":
            if cnt2>=cnt1+left:
                left=cnt2-cnt1

res=S.count("(")+left-S.count(")")
if res>=0:
    print("("*left+S+")"*res)
else:
    print("("*(left+abs(res))+S)