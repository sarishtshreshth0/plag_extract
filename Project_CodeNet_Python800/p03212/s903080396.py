from collections import deque, Counter

N = input()
l = len(N)

h = deque(['3','5','7'])
rlt = 0

while h:
  a = h.popleft()
  if int(N) >= int(a):
    dic = Counter(a)
    if dic['3'] > 0 and dic['5'] > 0 and dic['7'] > 0:
      rlt += 1
  if len(a) < l:
    for s in ('3','5','7'):
      h.append(a+s)
      
print(rlt)