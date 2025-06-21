def main():
    n, a, b = map(int, input().split())
    s = input()
    foreign, passed = 0, 0

    for i in range(len(s)):
        if s[i] == "a":
            if passed < a + b:
                print("Yes")
                passed += 1
            else:
                print("No")
        elif s[i] == "b":
            if passed < a + b and foreign < b:
                print("Yes")
                passed += 1
                foreign += 1
            else:
                print("No")
        else:
            print("No")


if __name__ == "__main__":
    main()
