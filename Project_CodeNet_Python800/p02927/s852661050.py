M, D = map(int, input().split())
count = 0

for i in range(22, D+1):
  d1 = i % 10
  d10 = i // 10
  m = d1 * d10
  if (m <= M) and (d1 >= 2):
    count += 1
    #print(m, i)
print(count)