MM = input().split()
A = int(MM[0])
B = int(MM[1])
S = input()
SS = '1234567890'
SSS =list(SS)
count = 0
for i in range(A):
  if S[i] not in SSS:
    count +=1
if S[A] != '-':
  count +=1
for i in range(A+1,A+B):
  if S[i] not in SSS:
    count +=1
if count ==0:
  print('Yes')
else:
  print('No')