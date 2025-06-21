S=input()
N=int(S)
cnt=0
def rec(l,x,N):
    global cnt
    if  len(l)==x:
        tmp=int("".join(map(str,l)))
        if tmp<=N and len(set(l))==3:
            cnt+=1
    else:
        for n in range(3):
            l.append(3+2*n)
            rec(l,x,N)
            l.pop()

for n in range(3,len(S)+1):
    rec([],n,N)
print(cnt)