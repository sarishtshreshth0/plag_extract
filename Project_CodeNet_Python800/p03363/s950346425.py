N = int(input())
A = list(map(int,input().split()))
S = [0]
for i in range(N):  S.append(S[-1] + A[i])
ans = 0
dic = {}
for data in S:
    if data in dic:  
        ans += dic[data]
        dic[data] += 1
    else:  dic[data] = 1
print(ans)