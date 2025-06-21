import collections
N = int(input())
*A, = map(int, input().split())
print(max(collections.Counter(A + [a-1 for a in A] + [a+1 for a in A]).values()))