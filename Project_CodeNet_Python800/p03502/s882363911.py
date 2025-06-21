n = input()


def digit(digits):
    result = 0
    for digit in digits:
        result += int(digit)

    return result

if int(n) % digit(n):
    print('No')
else:
    print('Yes')