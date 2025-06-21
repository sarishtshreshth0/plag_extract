A, B = map(int, input().split())

if A == 0:
  print(B)
  exit()
  
a = A - 1
rlt = ((B+1)//2 - (a+1)//2) % 2

for i in range(1, 40):
  pw1 = 2**i
  pw2 = pw1*2
  cnta = max(a % pw2 - pw1 + 1, 0)
  cntB = max(B % pw2 - pw1 + 1, 0)
  rlt += ((cntB - cnta) % 2)*pw1
  
print(rlt)