N = int(input())
List = list(map(int, input().split()))
S2 = 0
for i in range(N):
  S2 += List[i]
S1 =0 
res = S2
for i in range(N):
  S1 += List[i]
  S2 = S2 - List[i]
  res = min(abs(S2-S1),res)
print(res)