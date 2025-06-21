def main():
    a, b = map(int, input().split())
    s = input()

    for i in range(a + b + 1):
        if i == a:
            if s[i] != "-":
                print("No")
                exit()
        else:
            if not "0" <= s[i] <= "9":
                print("No")
                exit()
    else:
        print("Yes")


if __name__ == "__main__":
    main()
