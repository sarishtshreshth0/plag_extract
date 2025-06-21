def part(n):
    n = int(n)
    num1 = n/10
    num2 = n % 10
    return num1, num2


def final():
    months, days = map(int, input().split())

    count = 0
    for month in range(1, months+1):
        for day in range(0, days+1):
            x, y = part(day)
            x = int(x)
            y = int(y)
            if x >= 2 and y >= 2 and (x*y) == month:
                count += 1

    print(count)


if __name__ == "__main__":
    final()
