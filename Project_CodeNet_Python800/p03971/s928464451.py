N,A,B = map(int,input().split())
l = list(input())
num = 0
count = 0
for i in range(N):
  if l[i] == 'a' and A + B > num:
    print('Yes')
    num += 1
  elif l[i] == 'b' and (A + B > num):
    count += 1
    if count <= B:
      print('Yes')
      num += 1
    else:
      print('No')
  else:
    print('No')