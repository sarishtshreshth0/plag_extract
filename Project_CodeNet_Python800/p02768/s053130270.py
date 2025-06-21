n, a, b = map( int, input().split() )
mod = 10 ** 9 + 7

N = pow( 2, n, mod ) - 1

def comb( n, r  ):
  c = 1
  m = 1
  r = min( n - r, r )
  for i in range( r ):
    c = c * ( n - i ) % mod
    m = m * ( i + 1 ) % mod
  return c * pow( m, mod - 2, mod ) % mod

A = comb( n, a )
B = comb( n, b )
print( ( N - A - B ) % mod )