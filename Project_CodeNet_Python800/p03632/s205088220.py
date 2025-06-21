a,b,c,d=map(int,input().split())
S,F,countS,countF = 0,0,0,0
if a<=c:
  countS = c
  S = a
else:
  countS = a
  S = c
if b <= d:
  countF = b
  F = d
else:
  countF = d
  F = b
count=0
flagC = False
for i in range(S,F+1):
  if flagC:
    count+=1
  if i == countS:
    flagC = True
  if i == countF:
    break
print(count)