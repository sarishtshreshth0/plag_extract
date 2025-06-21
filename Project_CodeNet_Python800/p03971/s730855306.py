N, A, B = map(int, input().split())
S = input()
 
ok_count = 0
ok_fcount = 0
for i in range(N):
  if S[i] == 'a':
    if ok_count < A+B:
      print('Yes')
      ok_count +=1
      
    else:
      print('No')
      
  elif S[i] == 'b':
    if ok_count < A+B and ok_fcount < B:
      print('Yes')
      ok_count+=1
      ok_fcount+=1
      
    else:
      print('No')
      
  else:
    print('No')