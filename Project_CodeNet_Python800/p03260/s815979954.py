def main():
    a, b = (int(i) for i in input().split())
    ans = a*b
    if any(a*b*c % 2 == 1 for c in range(1, 4)):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
