# ABC137 D
import heapq

N,M=map(int,input().split())
AB=[]
for _ in [0]*N:
    a,b=map(int,input().split())
    AB.append((-a,-b))
AB.sort()
AB=[(-a,-b) for a,b in AB]

res=0
num=0
work=[]
hard=[0]*(M+1)
for a,b in AB:
    #a日後のしごとの話をしている→M-a+1件まで受注可能
    if num<M-a+1:
        # 仕事に余裕はある
        heapq.heappush(work,(b,a))
        hard[a]+=1
        res+=b
        num+=1
    else:
        # 仕事は十分持っている
        heapq.heappush(work,(b,a))
        c,d=heapq.heappop(work)
        res+=b-c
print(res)