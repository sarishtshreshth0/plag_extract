N = int( input() )
D = list ( int(x) for x in input().split() )

if D[0] != 0:
    ans = 0
else:
    Ds = [ 0 for i in range( max(D) + 1 ) ]

    for i in range( N ):
        Ds[ D[i] ] += 1

    ans = 1

    if Ds[ 0 ] != 1:
        ans = 0
    else:
        for i in range( 1 , max(D) + 1 ):
            ans *= Ds[ i-1 ] ** Ds[i]

            if ans == 0:
                break


print( ans % 998244353 )