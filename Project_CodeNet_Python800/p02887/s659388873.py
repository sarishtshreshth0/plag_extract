def main():
    N = int(input())
    S = input().rstrip()
    current_char = S[0]
    ans = 1
    for idx in range(1, N):
        if S[idx] != current_char:
            ans += 1
            current_char = S[idx]
    print(ans)


if __name__ == '__main__':
    main()
