# coding: utf-8

def main():
    h, w = map(int, input().split())

    if h == 1 or w == 1:
        ans = 1
    elif h * w % 2 == 0:
        ans = h * w // 2
    else:
        ans = h * w // 2 + 1

    print(ans)


if __name__ == "__main__":
    main()
