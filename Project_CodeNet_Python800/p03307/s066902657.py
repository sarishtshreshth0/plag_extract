N = int(input())

for i in range(N,N*2+1,N):
  if i % 2 == 0 and i % N == 0:
    print(i)
    break