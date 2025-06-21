def distance(a_lst, b_lst):
    n = len(a_lst)
    tmp_distance = 0

    for i in range(n):
        a = a_lst[i]
        b = b_lst[i]

        tmp_distance += (a - b) ** 2

    distance = (tmp_distance) ** (1/2)
    return distance


def main():
    n, d = map(int, input().split())
    x_lst = [0] * n
    count = 0

    for i in range(n):
        x_lst[i] = list(map(int, input().split()))

    for i in range(n-1):
        a_lst = x_lst[i]

        for j in range(i+1, n):
            b_lst = x_lst[j]

            if distance(a_lst, b_lst) == int(distance(a_lst, b_lst)):
                count += 1

    print(count)


if __name__ == '__main__':
    main()