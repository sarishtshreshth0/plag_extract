from itertools import accumulate
N = int(input())
S = input()

m = -min(min(accumulate(1 if c == '(' else -1 for c in S)),0)
s = sum(1 if c == '(' else -1 for c in S)

print('('*m+S+')'*(s+m))
