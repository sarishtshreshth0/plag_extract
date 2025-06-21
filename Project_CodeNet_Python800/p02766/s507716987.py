def main():
    N, K = map(int, input().split())
    ans = 0
    temp = 1
    while N > 0:
        ans = (N % K) * temp + ans
        N = N // K
        temp = temp * 10
    ans = str(ans)
    print(len(ans))
main()