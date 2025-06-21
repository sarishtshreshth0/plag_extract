n=int(input())
ab=[list(map(int, input().split())) for _ in range(n)] 
cd=[list(map(int, input().split())) for _ in range(n)] 

#ab = sorted(ab, key=lambda x:x[1]*(-1))
ab.sort(key=lambda x: x[0],reverse=True)
ab.sort(key=lambda x: x[1],reverse=True)
cd=sorted(cd)

cnt=0
for i in range(n):#ab
    for j in range(len(cd)):#cd
        if ab[i][0]<cd[j][0] and ab[i][1]<cd[j][1]:
            cnt+=1
            cd.pop(j)
            break
print(cnt)