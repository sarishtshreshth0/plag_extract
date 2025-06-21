N = int(input())
L = list(map(int,input().split()))


S = [0,L[0]]
for i in range(1,N):
  temp = S[i]+L[i]
  S.append(temp)
dic ={}
for i in range(len(S)):
  if S[i] not in dic:
    dic[S[i]] = 1
  else:
    dic[S[i]] += 1
ans = 0    
for t in dic.values():
  ans += t*(t-1)//2
print(ans)