# C - Slimes
def main():
    n = int(input())
    s = input()
    p = ''
    ans = ''

    for v in s:
        if v != p:
            ans += v
            p = v
        else:
            continue
    print(len(ans))

if __name__ == "__main__":
    main()