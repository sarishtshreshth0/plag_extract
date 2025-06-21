n,*ww = open(0).read().split()

import sys
words = set()
prev = None
for w in ww:
    if w in words:
        print('No')
        sys.exit()
    words.add(w)
    
    if prev and prev[-1] != w[0]:
        print('No')
        sys.exit()
    prev = w
print('Yes')