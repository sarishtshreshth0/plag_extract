from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

n, m = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(m)]

xs = []
ys = []
for x, y, _ in xyz:
    x -= 1
    y -= 1
    xs.append(x)
    ys.append(y)

graph = csr_matrix(([1] * m, (xs, ys)), shape=(n, n))
num = connected_components(graph, connection="weak", return_labels=False)
print(num)
