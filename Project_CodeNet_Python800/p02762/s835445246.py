N, M, K = map(int, input().split())
friends = [0 for _ in range(N)]
blocks = [0 for _ in range(N)]

class Union():
    def __init__(self, N):
        self.Parent = []
        for i in range(N):
            self.Parent.append(-1)

    def root(self, A):
        if(self.Parent[A] < 0):
            return A
        else:
            self.Parent[A] = self.root(self.Parent[A])
            return self.Parent[A]

    def size(self, A):
        return int(-1 * self.Parent[self.root(A)])

    def connect(self, A, B):
        A = self.root(A)
        B = self.root(B)
        if (A == B):
            return False

        if(self.size(A) < self.size(B)):
            A, B = B, A
        self.Parent[A] += self.Parent[B]
        self.Parent[B] = A
        return True

uni = Union(N)
ans = []
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    friends[A] += 1
    friends[B] += 1
    uni.connect(A,B)

for i in range(K):
    C, D = map(int, input().split())
    C -= 1
    D -= 1
    if (uni.root(C) == uni.root(D)):
        blocks[C] += 1
        blocks[D] += 1

for i in range(N):
    ansi = max(0, uni.size(i) - friends[i] - blocks[i] - 1)
    ans.append(str(ansi))

print(" ".join(ans))


