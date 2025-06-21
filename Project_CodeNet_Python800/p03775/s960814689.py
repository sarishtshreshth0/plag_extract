def main():
    def f(a, b):
        sa = str(a)
        sb = str(b)
        return max(len(sa), len(sb))
    N = int(input())
    ans = 10**12
    for i in range(1, N+1):
        if N < i*i:
            break
        if N % i != 0:
            continue
        b = N//i
        ans = min(ans, f(i, b))
    print(ans)


if __name__ == '__main__':
    main()
