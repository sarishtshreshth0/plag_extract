import sys
import time
import math
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

M, D = map(int, input().split())
ans = 0
for m in range(1, M+1):
	for d in range(D+1):
		if d < 10:
			continue
		if d//10 >= 2 and d%10 >= 2 and (d//10)*(d%10) == m:
			ans += 1
print(ans)

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
