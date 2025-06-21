N = int(input())
W = [input() for i in range(N)]
 
WS = list(set(W))
cnt = 0
 
if len(WS) != len(W):
  cnt += 1
else:
  for i in range(N-1):
      if W[i][-1] != W[i+1][0]:
          cnt += 1
 
print('No' if cnt >0 else 'Yes')