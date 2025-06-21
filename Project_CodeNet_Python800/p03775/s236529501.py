n = int(input())

MAXN = 10 ** 5


def answer():
    minf = 10
    for a in range(1, MAXN + 1):
        if n % a == 0:
            b = n // a
            f = max(len(str(a)), len(str(b)))
            minf = min(minf, f)
    return minf


print(answer())
