N = int(input())
A = list()
for i in range(N-1):
  A.append(list(map(int, input().split())))
for i in range(N):
  ans = 0
  j = i
  while(j < N-1):
    C = A[j][0]
    S = A[j][1]
    F = A[j][2]
    
    if(S > ans):
      ans = S
    else:
      if(ans % F != 0):
        ans = ((ans//F)+1)*F
    ans += C
    j += 1
    
  print(ans)