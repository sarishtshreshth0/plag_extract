import sys
_,*W = open(0).read().split()

if len(set(W)) != len(W):
    print('No')
    sys.exit()

s = W[0][0]
for w in W:
    if s != w[0]:
        print('No')
        sys.exit()
    s = w[-1]

print('Yes')