M,D =map(int,input().split())
count = 0
for i in range(M):
  for j in range(D-21):
    a = int((j+22)/10)
    b = (j+22) - (a*10)
    if a >=2 and b>=2 and i+1 == a * b:
      count += 1
print(count)