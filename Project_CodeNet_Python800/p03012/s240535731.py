import sys
N = int(input())
array = list(map(int,input().split()))

result = sum(array)
for I in range(len(array)):
    tmp = abs(sum(array[0:I]) - sum(array[I:]))
    if result > tmp: result = tmp
print(result)