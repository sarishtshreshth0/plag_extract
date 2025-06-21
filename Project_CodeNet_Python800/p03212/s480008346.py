from itertools import *
N = int(input())
ans = 0

for i in product("0357",repeat=10):
  j = "".join(i)
  if "0" not in str(int(j)) and "3" in j and "5" in j and "7" in j and int(j)<=N:
    ans+=1

print(ans)