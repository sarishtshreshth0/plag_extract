def main():
    A, B, C, D = map(int, input().split())

    ans = max(0, min(B, D) - max(A, C))
    print(ans)


if __name__ == "__main__":
    main()
