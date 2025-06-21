m, d = input().split()

if len(d) == 1:
  print(0)
  exit()

result = 0

for month in range(int(m)):
  for day in range(10, int(d)):
    d_1, d_10 = map(int, str(day+1))
    if 2 <= d_1 and 2 <= d_10 and d_1 * d_10 == month+1:
      result += 1
    
print(result)