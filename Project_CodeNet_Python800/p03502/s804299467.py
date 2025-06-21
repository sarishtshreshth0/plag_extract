#-------------
N = int(input())
#-------------
N_1 = N
F = []
while True :
  if N_1 != 0:
    F.append(N_1%10)
    N_1 = N_1//10
  else:
    break
ans = 0  
for i in range(len(F)):
  ans += F[i]

if N%ans == 0:
  print("Yes")
else:
  print("No")