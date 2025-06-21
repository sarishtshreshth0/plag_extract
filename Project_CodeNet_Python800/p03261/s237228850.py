def main():
    has_said = set()
    n = int(input())
    last = ""
    for i in range(n):
        w = input()
        if i > 0 and (w[0] != last or w in has_said):
            print("No")
            break
        last = w[-1]
        has_said.add(w)
    else:
        print("Yes")


if __name__ == '__main__':
    main()

