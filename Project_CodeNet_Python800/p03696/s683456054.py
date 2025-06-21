def main():
    n = int(input())
    S = input()
    left_shortage = 0
    now = 0
    for s in S:
        if s == "(":
            now += 1
        else:
            now -= 1
            left_shortage = min(now, left_shortage)

    right_shortage = 0
    now = 0
    for s in S[::-1]:
        if s == ")":
            now += 1
        else:
            now -= 1
            right_shortage = min(now, right_shortage)

    print("("*-left_shortage + S + ")"*-right_shortage)


if __name__ == "__main__":
    main()
