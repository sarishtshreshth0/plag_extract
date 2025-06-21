def solve():
    N = input()
    f = sum(list(map(int, list(N))))
    N = int(N)

    if N % f == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    solve()