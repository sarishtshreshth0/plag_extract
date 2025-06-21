A, B = map(int, input().split())
S = input()
NUMS = "0123456789"
flg = True
for i in range(A):
  flg *= (S[i] in NUMS)
flg *= (S[A] == '-')
for i in range(A, A+B):
  flg *= (S[i+1] in NUMS)
if flg:
  print("Yes")
else:
  print("No")