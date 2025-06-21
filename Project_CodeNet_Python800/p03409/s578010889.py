import bisect

N=int(input())
ab=[[0,0,0] for _ in range(N)]#x,y,used
cd=[[0,0,0] for _ in range(N)]

for i in range(N):
    ab[i][0],ab[i][1]=map(int,input().split())

for i in range(N):
    cd[i][0],cd[i][1]=map(int,input().split())
    
    
    
ab.sort()
cd.sort()
ans=0

for i in range(N):#各青に対して，
    temp_j=-1
    temp_y=-1
    for j in range(N):
        if ab[j][2]==0:#未使用ならば
            if ab[j][0] < cd[i][0]: #x座標が小さい中で
                if cd[i][1] > ab[j][1] and ab[j][1]>=temp_y:#y座標が最大のものを選ぶ
                    temp_y=ab[j][1]
                    temp_j=j
    if temp_j!=-1:
        ab[temp_j][2]=1
        ans+=1
        
print(ans)
        


