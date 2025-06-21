MM = input().split()
N = int(MM[0])
K = int(MM[1])
for i in range(1000000000000):
  if K**i > N:
    print(i)
    break
