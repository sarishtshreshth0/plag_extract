a,n = map(int,input().split())
point = []
for i in range(a):
  linea = list(map(int,input().split()))
  point.append(linea)

counta = 0
for j in range(a):
  for k in range(j+1,a):
    dist = 0
    for l in range(n):
      dist += (point[j][l] - point[k][l])**2

    if dist**0.5 == int(dist**0.5):
      counta += 1

print(counta)