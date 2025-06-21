def main():
    N = input_int()
    S = input()

    count = 1

    for i in range(1, N):
        if S[i-1] != S[i]:
            count += 1

    print(count)


def input_int():
    return int(input())


# def input_int_tuple():
#     return map(int, input().split())


# def input_int_list():
#     return list(map(int, input().split()))


main()
