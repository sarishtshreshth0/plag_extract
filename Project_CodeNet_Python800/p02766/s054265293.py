N,K = map(int,input().split())

i = 0
while True:
  if N >= K ** i:
    i += 1
  else:
    break

print(i)