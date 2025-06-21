import math
h,w = map(int,input().split())
ans = 0

if h == 1 or w ==1 :
  ans += 1

else:
    #奇数行目+偶数行目
    ans += math.ceil(h/2)*math.ceil(w/2)+(h//2)*(w//2)
 
print(ans)