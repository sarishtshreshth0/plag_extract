from collections import Counter

n = int(input())
A = list(map(int, input().split()))
sumA = [0]
for i in range(n):
    sumA.append(sumA[-1]+A[i])

ans = 0
csumA = Counter(sumA)
for key in csumA.keys():
    if csumA[key] > 1:
        ans += csumA[key]*(csumA[key]-1)//2
print(ans)