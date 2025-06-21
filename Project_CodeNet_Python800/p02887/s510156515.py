N = int(input())
S = input()

minus = 0
for i in range(1,N):
  if S[i-1] == S[i]:
    minus += 1

print(N - minus)