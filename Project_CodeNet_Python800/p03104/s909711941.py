def main():
    a, b = map(int, input().split())

    # if the number of 1 is odd: 1
    # else: 0
    b += 1
    ans = 0
    unit = 1
    for i in range(b.bit_length()):
        new_unit = unit << 1
        cnt = min(new_unit - a % new_unit, unit) % 2
        cnt += max(0, b % new_unit - unit) % 2
        cnt %= 2
        if cnt:
            ans += unit

        unit = new_unit

    if (b - a) % 2 == 0:
        if ((b - a) // 2) % 2 == 0:
            ans -= 1
    else:
        if a % 2 == 1:
            if ((b - a + 1) // 2) % 2 == 0:
                ans -= 1
        else:
            if ((b - a - 1) // 2) % 2 == 0:
                ans -= 1

    print(ans)

main()