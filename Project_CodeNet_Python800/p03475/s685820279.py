import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    CSF = []
    for i in range(N-1):
        c, s, f = map(int, input().strip().split())
        CSF.append((c, s, f))
    return N, CSF


def solve(N, CSF, SMAX=200000):
    A = []
    for c, s, f in CSF:
        for i in range(len(A)):
            if A[i] % f == 0:
                A[i] = max(A[i], s) + c
            else:
                A[i] = max(A[i] - A[i] % f + f, s) + c
        A.append(s + c)
    A.append(0)
    for a in A:
        print(a)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
