N, K = map(int, input().split())

bit = 0
while(N >= K**bit):
  bit += 1
print(bit)