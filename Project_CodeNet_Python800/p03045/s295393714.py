import numpy as np
from scipy.sparse import csr_matrix, csgraph
N, M = map(int, input().split())
row, column, _ = np.array([tuple(map(lambda n: int(n) - 1, input().split())) for _ in range(M)], dtype=np.int32).T
matrix = csr_matrix(([1] * M, (row, column)), shape=(N, N), dtype=np.int32)
print(csgraph.connected_components(matrix)[0])
