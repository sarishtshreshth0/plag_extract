N = int(input())
mn=100
for A in range(1,int(N**(0.5))+1):
    cnta=0
    cntb=0
    if N%A==0:
        B=N/A
        while A>0:
            A//=10
            cnta+=1
        while B>0:
            B//=10
            cntb+=1
        cnt=max(cnta,cntb)
        mn=min(mn,cnt)
print(mn)