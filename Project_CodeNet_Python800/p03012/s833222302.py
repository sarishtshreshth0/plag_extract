N = int(input())
WL = list(map(int, input().split()))
Aw = sum(WL)
Ow = 0
AL = []
for i in range(N):
    Ow += WL[i]
    ans = abs(Ow - (Aw -Ow))
    AL.append(ans)
print(min(AL))