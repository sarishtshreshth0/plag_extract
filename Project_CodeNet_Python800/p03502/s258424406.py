N = input()

n = list(N)

for i in range(len(n)):
  n[i] = int(n[i])

m = int(N)
if m % sum(n) == 0:
  print("Yes")
else:
  print("No")