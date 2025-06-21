n=int(input())
ng=['!']
for i in range(n):
  w=input()
  ng[0]+=w[0]
  if w in ng or w[0] != ng[-1][-1]:
    #print(w,ng[-1])
    print('No')
    break
  ng.append(w)
else:
  print('Yes')