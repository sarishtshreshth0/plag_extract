from itertools import accumulate
n=int(input())
w=list(map(int,input().split()))
w=list(accumulate(w))
for i in range(n):
  if w[i]*2==w[-1]:
    print(0)
    break
  elif w[i]*2>w[-1]:
    print(min((w[i]*2-w[-1]),(w[-1]-w[i-1]*2)))
    break