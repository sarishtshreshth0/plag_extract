import numpy as np
S = list(input())
S_np = np.array(list(map(int, S)))

standard1 = np.array([i%2 for i in range(len(S))])
standard2 = np.array([(i+1)%2 for i in range(len(S))])

diff_standard1 = sum((S_np - standard1) != 0)
diff_standard2 = sum((S_np - standard2) != 0)

print(min(diff_standard1, diff_standard2))