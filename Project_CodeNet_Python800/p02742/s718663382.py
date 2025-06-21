H, W = map(int, input().split())

if H==1 or W==1:
  # コーナーケース
  ans = 1

elif H%2==0 or W%2==0:
  ans = int(H*W/2)

else:
  ans = int((H*W+1)/2)

print(ans)