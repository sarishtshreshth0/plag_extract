from sys import stdin
H,W = [int(x) for x in stdin.readline().rstrip().split()]
#print(H,W)

#1,3,5...行目で塗れるマス
n_odd = (1+W)//2
#2.4,6...行目で塗れるマス
n_even = W//2

if W == 1 or H == 1:
  print(1)
  exit()


if H%2 == 0:
  ans = int((n_odd + n_even) * (H/2))
else:
  ans = int((n_odd + n_even) * (H-1)/2 + n_odd)

print(ans)