N = int(input())
a = list(map(int,input().split()))

import collections
c = collections.Counter(a)
ans = 0

if len(c) == 1:
  ans = list(c.values())[0]
else:
  for x in range(min(a),max(a)):
    ans_candidate = c[x] + c[x+1] + c[x+2]

    if ans < ans_candidate:
      ans = ans_candidate
print(ans)
