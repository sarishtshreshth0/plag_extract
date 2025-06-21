mod = 10**9 +7
n, a, b = map(int, input().split())

nb = str(bin(n))[2:]
nblis = []
for k in range(len(nb)):
  if nb[-k-1] == '1':
    nblis.append(k)

two = [2]
for k in range(len(nb)-1):
  two.append(two[-1]*two[-1]%mod)


ans = 1
for item in nblis:
  ans = ans * two[item] %mod



bi = str(bin(mod-2))[2:]
blis = []
for k in range(len(bi)):
  if bi[-k-1] == '1':
    blis.append(k)


def modinv(N):
  if N == 1:
    return 1
  else:
    res = 1
    li = []
    for _ in range(len(bi)):
      li.append(N%mod)
      N = N*N%mod
    for item in blis:
      res = res * li[item] %mod
    return res

ans_a = 1
for k in range(n-a+1, n+1):
  ans_a = ans_a*k%mod
for k in range(2, a+1):
  ans_a = ans_a*modinv(k)%mod


ans_b = 1
for k in range(n-b+1, n+1):
  ans_b = ans_b*k%mod
for k in range(2, b+1):
  ans_b = ans_b*modinv(k)%mod

print((ans-ans_a-ans_b-1)%mod)