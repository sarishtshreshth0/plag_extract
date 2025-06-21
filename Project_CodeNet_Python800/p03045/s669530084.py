import numpy as np
from scipy.sparse import csr_matrix, csgraph
N, M = map(int, input().split())
print(csgraph.connected_components(csr_matrix(([1] * M, (np.array([tuple(map(lambda n: int(n) - 1, input().split()[:2])) for _ in range(M)], dtype=np.int32).T)), shape=(N, N), dtype=np.int32), return_labels=False))
