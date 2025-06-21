X = int(input())
ans = 0
if X >= 500:
  ans += (X//500)*1000
  ans += ((X%500)//5)*5
else:
  ans += (X//5)*5
print(ans)