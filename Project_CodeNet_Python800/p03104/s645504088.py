def main():
    a, b = list(map(int, input().split()))
    if b - a <= 3:
        ans = a
        for i in range(a + 1, b + 1):
            ans = ans ^ i
        print(ans)
    else:
        if a % 4 == 0:
            ans = 0
        elif a % 4 == 1:
            ans = a ^ (a + 1) ^ (a + 2)
        elif a % 4 == 2:
            ans = a ^ (a + 1)
        else:
            ans = a
        if b % 4 == 0:
            ans = ans ^ b
        elif b % 4 == 1:
            ans = ans ^ (b - 1) ^ b
        elif b % 4 == 2:
            ans = ans ^ (b - 2) ^ (b - 1) ^ b
        else:
            ans = ans ^ (b - 3) ^ (b - 2) ^ (b - 1) ^ b
        print(ans)



if __name__ == '__main__':
    main()
