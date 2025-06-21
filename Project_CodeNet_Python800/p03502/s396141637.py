import sys
N = int(input())
array_N = list(map(int,str(N)))

if not (1 <= N <= 10 ** 8):
    sys.exit()

sum_array_N = 0
for I in range(len(array_N)):
    sum_array_N += array_N[I]

if N % sum_array_N == 0:
    print("Yes")
else:
    print("No")