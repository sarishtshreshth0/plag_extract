import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N = in_n()
    csf = [tuple(in_nn()) for _ in range(N - 1)]

    for i in range(N - 1):
        c, s, f = csf[i]
        time = c + s
        for j in range(i + 1, N - 1):
            c, s, f = csf[j]
            if time <= s:
                time = s + c
            else:
                r = (time - s) % f
                if r != 0:
                    time += f - r
                time += c
        print(time)
    print(0)


if __name__ == '__main__':
    main()
