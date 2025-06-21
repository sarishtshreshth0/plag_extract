N,M = list(map(int,input().split()))
X = list(map(int,input().split()))
sortedX = sorted(X)
deltaList = []
for i in range(len(sortedX) - 1):
    delta = sortedX[i + 1] - sortedX[i]
    deltaList.append(delta)
sortedDeltaList = sorted(deltaList)
answer = 0
count = M - 1 - N + 1
if count <= 0:
    answer = 0
else:
    for i in range(count):
        answer += sortedDeltaList[i]
print(answer)