n=int(input())
kotaezyun=[]
renketu=[[] for i in range(n+1)]
ans_dict={}
for i in range(n-1):
    a,b=map(int, input().split())
    renketu[a].append(b)
    kotaezyun.append([a,b])

from collections import deque
que=deque()

que.append(1)

iro=[-1]*(n+1)
iro[1]=0
irokazu=0

tansaku_moto=[1]

while que:
    tansaku_moto=que.popleft()
    ironuri=1
    for tansaku_saki in renketu[tansaku_moto]:
        if ironuri==iro[tansaku_moto]:
            ironuri+=1
        iro[tansaku_saki]=ironuri
        ans_dict[tansaku_moto,tansaku_saki]=ironuri
        que.append(tansaku_saki)
        irokazu=max(irokazu,ironuri)
        ironuri+=1
        
print(irokazu)
for i in range(n-1):
    tmp=(kotaezyun[i][0],kotaezyun[i][1])
    print(ans_dict[tmp])