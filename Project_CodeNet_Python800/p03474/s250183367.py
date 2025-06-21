A,B=map(int,input().split())
S=input()

if len(S) != A+B+1:
  print(0)
  print('No')
  exit()
  
for i in range(A):
  if S[i] not in set(map(str,list(range(10)))):
    print('No')
    exit()
if S[A] != '-':
  print('No')
  exit()
for i in range(A+1,A+B+1):
  if S[i] not in set(map(str,list(range(10)))):
    print('No')
    exit()
print('Yes')