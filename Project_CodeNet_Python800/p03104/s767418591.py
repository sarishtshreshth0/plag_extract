def F(X):
    if X % 4 == 1:
        return 1
    if X % 4 == 2:
        return X + 1
    if X % 4 == 3:
        return 0
    if X % 4 == 0:
        return X


def test():
    x = 0
    for i in range(1, 50):
        x ^= i
        print(i, ":", x)


if __name__ == "__main__":
    A, B = map(int, input().split())
    if A == 0:
        print(F(B))
    else:
        print(F(B) ^ F(A-1))