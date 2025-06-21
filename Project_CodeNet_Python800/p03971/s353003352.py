
def resolve():
    n, a, b = input().strip().split(' ')
    n, a, b = [int(n), int(a), int(b)]
    s = input().strip()
    a_passed = 0
    b_passed = 0
    for i in range(len(s)):
        if s[i] == 'a':
            if a_passed + b_passed < a + b:
                a_passed = a_passed + 1
                print('Yes')
            else:
                print('No')
        elif s[i] == 'b':
            if a_passed + b_passed < a + b and b_passed < b:
                b_passed = b_passed + 1
                print('Yes')
            else:
                print('No')
        else:
            print('No')
resolve()
