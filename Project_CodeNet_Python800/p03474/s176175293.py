a,b,s = open(0).read().split()

if (int(a), int(b)) == tuple(map(len, s.split('-'))):
    print('Yes')
else:
    print('No')