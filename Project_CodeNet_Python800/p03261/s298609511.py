N=int(input())
p=['6']
ans='Yes'
for i in range(N):
  W=input()
  if i!=0:
    if p[-1][-1]!=W[0]:
      ans='No'
      break
  if W in p:
    ans='No'
    break
  else:
    p.append(W)
print(ans)