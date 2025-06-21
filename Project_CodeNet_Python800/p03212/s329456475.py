N=input()
n=int(N)
from itertools import product
print(sum([sum(["3" in p and "5" in p and "7" in p and int(''.join(p))<=n for p in product("357",repeat=i+1)]) for i in range(len(N))]))