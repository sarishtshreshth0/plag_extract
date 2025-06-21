N, K = map(int, input().split())

num = ""
while(N > 0):
  num += str(N % K)
  N = int(N / K)

print(len(num))