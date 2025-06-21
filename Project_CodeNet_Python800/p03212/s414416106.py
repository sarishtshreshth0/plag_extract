N = input()
l = len(N)


def func(i, flag, b, only_leading_zero):
    if i == l:
        if b == 7:
            return 1
        else:
            return 0

    sum_ = 0
    flag_temp = flag
    for n in (0, 3, 5, 7):
        if not only_leading_zero and n == 0:
            continue

        if not flag and n > int(N[i]):
            continue

        if not flag and n < int(N[i]):
            flag = True

        if n == 3:
            x = 0b001
            only_leading_zero = False
        elif n == 5:
            x = 0b010
            only_leading_zero = False
        elif n == 7:
            x = 0b100
            only_leading_zero = False
        else:
            x = 0b000

        sum_ += func(i + 1, flag, b | x, only_leading_zero)
        flag = flag_temp

    return sum_


r = func(0, False, 0, True)
print(r)
