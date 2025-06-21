n=int(input())
csf=[list(map(int, input().split())) for _ in range(n-1)]

l=[]
for i in range(n-1):
    cnt=0
    for j in range(i,n-1):
        if cnt>=csf[j][1]:
            tmp_cnt=(cnt-csf[j][1]-1)//csf[j][2]
            cnt=csf[j][1]+(tmp_cnt+1)*csf[j][2]
        else:
            cnt=csf[j][1]
        cnt+=csf[j][0]
    l.append(cnt)

l.append(0)
for l_i in l:
    print(l_i)
