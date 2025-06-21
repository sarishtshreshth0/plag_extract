N=input()
l=len(N)
N=int(N)
if l<3:
    print(0)
else:
    
    cands=[None]*(l+1)
    cands[0]={}
    cands[1]={}
    cands[2]={}
    cands[3]= {"357","375","537","573","735","753"}
    
    for i in range(3,l):
        cands[i+1] = set(s+c for c in cands[i] for s in ["3","5","7"]) | set(c+s for c in cands[i] for s in ["3","5","7"] )
        cands[i+1].add("3"+"5"*(i-1)+"7")
        cands[i+1].add("3"+"7"*(i-1)+"5")
        cands[i+1].add("5"+"3"*(i-1)+"7")
        cands[i+1].add("5"+"7"*(i-1)+"3")
        cands[i+1].add("7"+"3"*(i-1)+"5")
        cands[i+1].add("7"+"5"*(i-1)+"3")
    
    ans=sum( [len(cands[i]) for i in range(l)] )
    ans+=sum( int(c)<=N for c in cands[l])
    print(ans)