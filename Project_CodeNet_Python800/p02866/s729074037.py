n = int(input())
dl = list(map(int,input().split()))
if dl[0] != 0:
  print(0)
  exit()
d_dic = dict()
for d in dl:
  if d in d_dic:
    d_dic[d] += 1
  else:
    d_dic[d] = 1
l = max(d_dic.keys())
for i in range(l):
  if not i in d_dic:
    print(0)
    exit()
if d_dic[0] != 1:
  print(0)
  exit()
ans = 1
for i in range(l):
  ans *= d_dic[i]**d_dic[i+1]
  ans = ans%998244353
print(ans)