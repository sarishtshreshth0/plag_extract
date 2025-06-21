import numpy as np
N,D = (int(x) for x in input().split())
X = np.zeros((N,D),dtype=int)
for I in range(0,N):
    X[I,:] = np.array([int(x) for x in input().split()],dtype=int)
    
Count = 0
for I in range(0,N-1):
    for II in range(I+1,N):
        if np.linalg.norm(X[I,:]-X[II,:]).is_integer():
            Count += 1
print(Count)