H,W = map(int,input().split())

if((H != 1)and(W != 1)):
  cnt1 = ((H+1)//2)*((W+1)//2)
  cnt2 = (H//2)*(W//2)
  ans = cnt1 + cnt2
else:
  ans = 1
  
print(ans)