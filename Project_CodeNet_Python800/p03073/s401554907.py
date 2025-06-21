S = input()
T1 = len(S)*"01"
T2 = len(S)*"10"
ans = []
dif = 0

for s,t in zip(S,T1):
  if s!=t:
    dif+=1

ans+=[dif]
dif = 0

for s,t in zip(S,T2):
  if s!=t:
    dif+=1

ans+=[dif]
print(min(ans))