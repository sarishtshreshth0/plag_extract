def main():
    N = int(input())
    A = map(int, input().split())

    ctr = [0] * (10 ** 5 + 2)  # [-1,10**5]
    for x in A:
        for j in range(-1, 2):
            ctr[x + j] += 1
    print(max(ctr))


if __name__ == '__main__':
    main()
