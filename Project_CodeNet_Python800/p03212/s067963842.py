n=int(input())
digits=len(str(n))
dlst=['3','5','7']
ans=0

for d in range(3,digits+1):
    for i in range(3**d):
        cur=[dlst[k] for k in [i//(3**j)%3 for j in range(d)]]
    
        cnt=[0]*3

        for j in range(d):
            for k in range(3):
                cnt[k]+=1 if dlst[k]==cur[j] else 0
        
        if cnt[0]*cnt[1]*cnt[2]==0 or int(''.join(cur))>n:
            continue

        ans+=1

print(ans)