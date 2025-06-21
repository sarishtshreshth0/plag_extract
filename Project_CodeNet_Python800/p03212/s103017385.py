from itertools import product
target = ['3','5','7']

n=int(input())
tmp=n
keta=0
while tmp!=0:
  tmp//=10
  keta+=1
check_list = []
for i in range(1,keta+1):
  tmp=[]
  for _ in range(i):
    tmp.append(target.copy())
    tmp_product = list(product(*tmp))
  check_list+=[int(''.join(nums)) for nums in tmp_product]
check_list = sorted(check_list)

cnt=0
for i in check_list:
  if i <= n:
    tmp = set([w for w in str(i)])
    if len(tmp)==3:
      cnt+=1
  else:
    break
print(cnt)
