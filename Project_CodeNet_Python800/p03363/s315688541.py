from collections import Counter

N = map(int, input().split())
As = list(map(int, input().split()))

lst = []
t = 0
for a in As:
  t += a
  lst.append(t)
  
dic = Counter(lst)

rlt = 0
for k in dic:
  if k == 0:
    rlt += dic[k]
  rlt += (dic[k]-1)*dic[k]//2
  
print(rlt)