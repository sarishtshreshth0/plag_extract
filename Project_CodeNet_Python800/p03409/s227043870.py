# coding: utf-8


def solve(*args: str) -> str:
    n = int(args[0])
    R = [tuple(map(int, ab)) for ab in map(str.split, args[1:n+1])]
    B = [tuple(map(int, ab)) for ab in map(str.split, args[n+1:2*n+1])]

    R.sort(key=lambda x: (-x[1], x[0]))
    B.sort(key=lambda x: (x[0], x[1]))

    count = 0
    used = [False]*n
    for i in range(n):
        bx, by = B[i]
        for j in range(n):
            if used[j]:
                continue
            rx, ry = R[j]
            if rx < bx and ry < by:
                count += 1
                used[j] = True
                break

    return str(count)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
