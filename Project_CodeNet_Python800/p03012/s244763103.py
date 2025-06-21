N=int(input())
WList=list(map(int, input().split()))
ANS=max(WList)
for i in range(N):
    ANS=min((abs(sum(WList[:i])-sum(WList[i:]))),ANS)
print(ANS)