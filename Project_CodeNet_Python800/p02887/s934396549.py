N = int(input())
S = input()

cnt = 0
sum = len(S)


for i in range(N-1):

  
  if S[i] == S[i+1]:
  	cnt += 1
  else:
  	continue

ans = sum - cnt

print(ans)