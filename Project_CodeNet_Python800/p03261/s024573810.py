import sys
N = int(input())
W = [input() for _ in range(N)]
li = [W[0]]
for i in range(1,N):
  if W[i][0] != W[i-1][-1]:
    print("No")
    sys.exit()
  if W[i] in li:
    print("No")
    sys.exit()
  li.append(W[i])
print("Yes")