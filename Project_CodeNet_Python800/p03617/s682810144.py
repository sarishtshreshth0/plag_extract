def main():
    Q, H, S, D = map(int, input().split())
    N = int(input())
    Q4 = 4*Q
    H2 = 2*H
    D12 = D/2
    M = min(Q4, H2, S)
    if D12 < M:
        ans = (N//2)*D + (N%2)*M
    else:
        ans = N*M
    print(ans)

if __name__ == "__main__":
    main()
