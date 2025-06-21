import heapq
N,M = map(int,input().split())
AB_s = [list(map(int, input().split())) for _ in range(N)]
MAPperA = {i: [] for i in range(1,M+1)}
# 残り日数ごとのマップを作る
for i, AB in enumerate(AB_s):
    if AB[0] in MAPperA:
        MAPperA[AB[0]].append(AB[1])
excutableJobList = []
heapq.heapify(excutableJobList)
answer = 0
# 短期間でできる仕事からリストを作って追加してそーとして最大値を追加していく
for i in range(1,M+1):
    for j in MAPperA[i]:
        heapq.heappush(excutableJobList, j*-1)
    if excutableJobList:
        answer += heapq.heappop(excutableJobList) * -1
print(answer)