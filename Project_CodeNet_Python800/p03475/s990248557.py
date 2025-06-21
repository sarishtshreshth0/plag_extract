import sys

read = sys.stdin.buffer.read


def main():
    N, *CSF = map(int, read().split())
    train = [0] * (N - 1)
    for i, t in enumerate(zip(*[iter(CSF)] * 3)):
        train[i] = t

    ans = [0] * N
    for i in range(N - 1):
        t = 0
        for c, s, f in train[i:]:
            if t < s:
                t = s + c
            elif t % f == 0:
                t += c
            else:
                t += f - (t % f) + c
        ans[i] = t

    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()
