#区間の和を求める時は累積和を計算しておけば早く求まる
#それを全探索していても間に合わない(o(N^2))
#区間の和が０になる。累積和のリストに対してs_i-s_j=0になるようなs_iとs＿jの組みの総数は？
#累積和のリストをCounterで数えてnC2で計算すればいい
n=int(input())
a=list(map(int,input().split()))
from itertools import accumulate
from collections import Counter

a=[0]+list(accumulate(a))
a=Counter(a)
ans=0
for i in a:
  ans=ans+a[i]*(a[i]-1)//2
print(ans)
