def main():
    n = int(input())
    w_lst = list(map(int, input().split()))
    difference_lst = []

    for i in range(1, n):
        s1 = 0
        s2 = 0

        for j in range(i):
            s1 += w_lst[j]
        for j in range(i, n):
            s2 += w_lst[j]

        difference_lst.append(abs(s1 - s2))

    minimum = min(difference_lst)
    print(minimum)


if __name__ == '__main__':
    main()