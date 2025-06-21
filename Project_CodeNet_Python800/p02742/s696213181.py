import sys
from itertools import islice, tee


def resolve(in_):
    H, W = map(int, next(in_).split())
    h0, h1 = divmod(H, 2)
    w0, w1 = divmod(W, 2)

    if H == 1 or W == 1:
        return 1

    answer = h0 * w0 * 2
    if h1:
        answer += w0
    if w1:
        answer += h0
    if h1 and w1:
        answer += 1

    return answer


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
