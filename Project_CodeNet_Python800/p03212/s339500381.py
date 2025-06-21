import itertools

def main():
    N = int(input())
    if N < 100:
        print(0)
        exit()
    ans = 0
    for rep in range(3, len(str(N))+1):
        for comb in itertools.product(["3", "5", "7"], repeat=rep):
            if len(set(comb)) != 3:
                continue
            if int("".join(comb)) <= N:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
