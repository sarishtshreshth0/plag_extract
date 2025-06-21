N = int(input())
csf = [0] * (N - 1)

for i in range(N - 1):
  c, s, f = map(int, input().split())
  csf[i] = [c, s, f]
  
def depart(n):
  now_time = 0
  if n == N - 1:
    return 0
  while n != N - 1:
    next_st = csf[n]
    if now_time <= next_st[1]:
      now_time = next_st[1] + next_st[0]
    else:
      while now_time % next_st[2] != 0:
        now_time += 1
      now_time += next_st[0]
    n += 1
    #print(n, now_time)
  return now_time

for i in range(N):
  print(depart(i))
  
  
      
      
      
  
  
  
  
  
  

