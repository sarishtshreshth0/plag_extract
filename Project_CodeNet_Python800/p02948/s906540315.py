import heapq as hp

N, M = map( int, input().split() )
L = [[]] * M

for i in range( N ):
  a, b = map( int, input().split() )
  if a - 1 < M:
    if L[ a - 1 ] == []:
      L[ a - 1 ] = [ b ]
    else:
      L[ a - 1 ].append( b )
      
ret = 0
C = []
hp.heapify( C )
for i in range( M ):
  for i in L[i]:
    hp.heappush( C, -i)
  if C != []:
    ret -= hp.heappop( C )

print( ret )
