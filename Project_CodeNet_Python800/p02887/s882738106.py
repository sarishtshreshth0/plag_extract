def actual(n, s):
    count = 0
    last_color = ''

    for color in s:
        if last_color != color:
            last_color = color
            count += 1

    return count

n = int(input())
s = input()

print(actual(n, s))
