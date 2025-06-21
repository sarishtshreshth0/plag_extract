import copy

n = int(input())

judge = []
ans3 = 3
ans5 = 5
ans7 = 7
ans35 = []
ans37 = []
ans57 = []
ans357 = []

for i in range(8):
  key = []
  for v in ans357:
    key.append(v*10+3)
    key.append(v*10+5)
    key.append(v*10+7)
  for v in ans35:
    key.append(v*10+7)
  for v in ans37:
    key.append(v*10+5)
  for v in ans57:
    key.append(v*10+3)
  ans357 = copy.deepcopy(key)
  
  key = [ans3*10+5, ans5*10+3]
  for v in ans35:
    key.append(v*10+3)
    key.append(v*10+5)
  ans35 = copy.deepcopy(key)
    
  key = [ans3*10+7, ans7*10+3]
  for v in ans37:
    key.append(v*10+3)
    key.append(v*10+7)
  ans37 = copy.deepcopy(key)
  
  key = [ans5*10+7, ans7*10+5]
  for v in ans57:
    key.append(v*10+5)
    key.append(v*10+7)
  ans57 = copy.deepcopy(key)
  
  ans3 = ans3*10+3
  ans5 = ans5*10+5
  ans7 = ans7*10+7
  
  judge = judge+ans357
ans = 0
for v in judge:
  if v <= n:
    ans += 1
print(ans)