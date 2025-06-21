def solve():
    N,K = [int(i) for i in input().split()]

    digits = 1
    while N >= K:
        digits += 1
        N /= K

    print(digits)

if __name__ == "__main__":
    solve()