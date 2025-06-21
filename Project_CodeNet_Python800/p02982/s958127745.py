import sys
import itertools
N,D = map(int,input().split())
array = [ list(map(int,input().split())) for x in range(N) ]

if not ( 2 <= N <= 10 and 1 <= D <= 10 ): sys.exit()
for I in array:
    if not ( -20 <= min(I) and max(I) <= 20 ): sys.exit()

count = 0
for I in list(itertools.combinations(array,2)):
    tmp_distance = 0
    for J in range(D):
        tmp_distance += abs(I[0][J] - I[1][J]) ** 2
    distance = tmp_distance ** 0.5 
    if distance.is_integer(): count += 1

print(count)