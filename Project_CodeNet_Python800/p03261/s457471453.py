from collections import defaultdict
import sys
N = int(input())
W = [input() for _ in range(N)]

dict = defaultdict(bool)  # int/bool/list....
dict[W[0]] = True
for i in range(1, N):
    if (W[i][0] is not W[i - 1][-1]) or dict[W[i]]:
        print("No")
        sys.exit()
    dict[W[i]] = True

print("Yes")