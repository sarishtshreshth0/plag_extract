S = input()
N = len(S)
A = list(S)
a = 0
b = 0
for i in range(N):
  if i%2 == 0:
    #010101
    if S[i] != "0":
      a += 1
    #101010
    else:
      b += 1
  #mod2 = 1
  else:
    #010101
    if S[i] != "1":
      a += 1
    #101010
    else:
      b += 1
print(min(a,b))