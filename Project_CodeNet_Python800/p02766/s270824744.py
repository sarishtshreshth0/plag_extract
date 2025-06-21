import numpy

N, K = map(int, input().split())
print(len(numpy.base_repr(N, K)))
