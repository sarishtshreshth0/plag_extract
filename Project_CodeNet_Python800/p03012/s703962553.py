N = int(input())
NN = input().split()
mini = 100
for i in range(N):
  total1 =0
  total2 =0
  for j in range(i+1):
    total1 +=  int(NN[j])
  for k in range(i+1,N):
    total2 += int(NN[k])
  ans = abs(total1-total2)
  if mini >ans:
    mini =ans
print(mini)