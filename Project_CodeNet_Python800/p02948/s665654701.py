from heapq import heappush, heappop
 
N,M = map(int,input().split())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i],B[i] = map(int,input().split())
AB = [[] for _ in range(M+1)] # A に対する B
for a,b in zip(A,B):
    if a <= M:
        AB[a].append(b)
        
q = []
answer = 0

for day in AB:
    # 制限より短いものからも選べるように全文pushして一番良いものだけpopする
    for pay in day:
        heappush(q,-pay)
    if len(q) > 0:
        answer += -heappop(q)
        
print(answer)