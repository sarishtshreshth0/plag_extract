def main():
    n = int(input())
    As = list(map(int, input().split()))
    cnts = [0]*(10**5+2)
    for a in As:
        cnts[a] += 1
        cnts[a+1] += 1
        cnts[a+2] += 1
    ans = max(cnts)
    print(ans)


if __name__ == "__main__":
    main()
