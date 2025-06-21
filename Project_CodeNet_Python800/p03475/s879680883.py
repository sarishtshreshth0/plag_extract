N = int(input())
stations = [list(map(int, input().split())) for _ in range(N-1)]

import numpy as np
for i in range(N-1):
    elapsed_time = 0
    for k in range(i, N-1):
        c, s, f = stations[k]
        # 出発前での時間を求める
        if elapsed_time <= s:
            wait_time = s - elapsed_time
        else:
            x = elapsed_time - s
            next_train = f * np.ceil(x/f)
            wait_time = next_train - x
        elapsed_time += wait_time + c
    print(int(elapsed_time))
print(0)
