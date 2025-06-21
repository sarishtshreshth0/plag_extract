def main():
    n = int(input())
    w_list = [input() for _ in range(n)]

    if len(set(w_list)) != n:
        print("No")
        exit()

    for i in range(n - 1):
        if w_list[i][-1] != w_list[i + 1][0]:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
