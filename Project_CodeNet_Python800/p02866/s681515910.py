from collections import Counter

N = int( input() )
tree = list( map( int, input().split() ) )

c = Counter(tree)
if tree[0] != 0 or c[0] != 1:
    print(0)
else:
    ans = 1
    a = c[0]
    for i in range( 1,len(c)):
        t = c[i]
        if t == 0:
            print(0)
            exit()
        else:
            ans *= ( a**t )
            a = t
    print(ans%998244353)
