import numpy as np

N,D = map(int,input().split())
x = np.array([[int(i) for i in input().split()] for _ in range(N)])

count = 0
for i in range(N):
    for j in range(i+1,N):
        if float.is_integer(np.linalg.norm(x[i][:]-x[j][:], ord=2)):
            count += 1
print(count)
