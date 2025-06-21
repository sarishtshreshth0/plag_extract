N, K = map(int, input().split())

def dec2n(int1, int2):
  l = ""
  while int1 != 0:
    l += str(int1 % int2)
    int1 = int1 // int2
  return l[::-1]

if K == 10:
  print(len(str(N)))
else:
  print(len(dec2n(N, K)))