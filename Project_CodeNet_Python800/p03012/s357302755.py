N = int(input())
W = [int(n) for n in input().split()]
W_ = [W[0]]

for i in range(1, N):
    W_.append(W_[-1] + W[i])
#print(W_)

d_min = 100000
for i in range(N):
    d = abs(2 * W_[i] - W_[-1])
    d_min = min(d_min, d)

print(d_min)
