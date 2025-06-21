def main():
    n = int(input())
    S = input()
    a, b = 0, 0
    aa = 0
    m = 0
    for s in S:
        if aa > 0 and s == ')':
            m += 1
            aa -= 1
        if s == '(':
            a += 1
            aa += 1
        else:
            b += 1
    print(''.join(['(' * (b - m), S, ')' * (a - m)]))

if __name__ == '__main__':
    main()
