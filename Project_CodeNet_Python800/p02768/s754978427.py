mod = 10**9 +7
n, a, b = map(int, input().split())

lis = []
on = 0 + n
count = 0
while on > 0:
  if on & 1 == 1:
    lis.append(count)
  count += 1
  on >>= 1

two = [2]
for _ in range(count-1):
  two.append(two[-1]*two[-1]%mod)

ans = 1
for item in lis:
  ans = ans * two[item] %mod

op = mod-2
invlis = []
count = 0
while op > 0:
  if op & 1 == 1:
    invlis.append(count)
  count += 1
  op >>= 1


def modinv(N):
  if N == 1:
    return 1
  else:
    res = 1
    Nlis = []
    for _ in range(count):
      Nlis.append(N%mod)
      N = N*N%mod
    for item in invlis:
      res = res * Nlis[item] %mod
    return res

ans_a = 1
for k in range(n-a+1, n+1):
  ans_a = ans_a*k%mod
amother = 1
for k in range(2, a+1):
  amother = amother * k % mod
ans_a = ans_a*modinv(amother)%mod

ans_b = 1
for k in range(n-b+1, n+1):
  ans_b = ans_b*k%mod
bmother = 1
for k in range(2, b+1):
  bmother = bmother * k % mod  
ans_b = ans_b*modinv(bmother)%mod

print((ans-ans_a-ans_b-1)%mod)