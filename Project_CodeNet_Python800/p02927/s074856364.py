A,B = map(int, input().split())
count = 0
for i in range(4,A+1):
  for j in range(22,B+1):
    C = str(j)
    if i == int(C[0])*int(C[1]) and int(C[1]) > 1:
      count = count + 1
print(count)

