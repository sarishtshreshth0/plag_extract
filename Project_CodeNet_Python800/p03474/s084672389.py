A, B = map(int, input().split())
S = input()


def is_digit(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


a = S[:A]
x = S[A]
b = S[A+1:]

if x == "-":
    for num in [a, b]:
        if not is_digit(num):
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")