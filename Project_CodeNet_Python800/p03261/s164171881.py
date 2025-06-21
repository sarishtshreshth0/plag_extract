N = int(input())
W = input()
L = [W]

for n in range(N-1):
  w = input()
  if W[-1] == w[0] and w not in L:
    L.append(w)
    W = w
  else:
    print("No")
    exit()
    
print("Yes")