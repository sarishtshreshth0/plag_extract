from fractions import gcd
class SegmentTree(object):
    def __init__(self, sequence, function, identity):
        N = len(sequence)
        self.length = (1 << (N - 1)).bit_length()
        self.data = [identity] * (self.length << 1)
        self.function = function
        self.identity = identity
        for i in range(N):
            self.data[i + self.length - 1] = sequence[i]
        for i in range(self.length - 2, -1, -1) :
            self.data[i] = self.function(self.data[(i << 1) + 1], self.data[(i << 1) + 2])

    def update(self, idx, x):
        idx += self.length - 1
        self.data[idx] = x
        while idx:
            idx = (idx - 1) >> 1
            self.data[idx] = self.function(self.data[(idx << 1) + 1], self.data[(idx << 1) + 2])

    def query(self, p, q):
        if q <= p:
            return self.identity
        p += self.length - 1
        q += self.length - 2
        res = self.identity
        while q - p > 1:
            if not p & 1:
                res = self.function(res, self.data[p])
            if q & 1:
                res = self.function(res, self.data[q])
                q -= 1
            p >>= 1
            q = (q - 1) >> 1
        return self.function(res, self.data[p]) if p == q else self.function(self.function(res, self.data[p]), self.data[q])

N, *A = map(int, open(0).read().split())
seg_tree = SegmentTree(A, gcd, 0)
ans = 0
for i in range(N):
    seg_tree.update(i, 0)
    ans = max(ans, seg_tree.query(0, N))
    seg_tree.update(i, A[i])
print(ans)