import numpy as np

N = int(input())
W = input().split()

for i in range(N):
    W[i] = int(W[i])
min_w= 1000000
for i in range(N-1):
    w1 = W[:i+1]
    w2 = W[i+1:]
    w1 = np.array(w1)
    w2 = np.array(w2)
    min_w = min(min_w, abs(np.sum(w2)-np.sum(w1)))

print(min_w)