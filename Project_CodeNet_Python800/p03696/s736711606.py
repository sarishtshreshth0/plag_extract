from collections import deque

N = int(input())
closings = list(input())
r_cnt = l_cnt = 0
for closing in closings:
  if closing == ')':
    if l_cnt > 0:
      l_cnt -= 1
    else:
      r_cnt += 1
  else:
    l_cnt += 1
answer = ['(' for _ in range(r_cnt)] + closings + [')' for _ in range(l_cnt)] 
print(''.join(answer))