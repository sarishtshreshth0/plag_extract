from collections import Counter
inputs = open(0).readlines()

n = int(inputs[0])
*D, = map(int, inputs[1].split())
mod = 998244353

nbs = [0] * (max(D)+1)
for k, v in Counter(D).items():
    nbs[k] = v

if D[0] != 0 or nbs[0] != 1:
    print(0)
else:
    ans = 1
    for n0, n1 in zip(nbs, nbs[1:]):
        ans = ans * pow(n0, n1, mod) % mod
    print(ans)