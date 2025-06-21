def resolve():
    A, B = list(map(int, input().split()))
    ans = A
    i = A + 1
    warped = False
    while i <= B:
        if not warped and i % 4 == 0:
            i = B - B%4
            warped = True
        else:
            ans = ans ^ i
            i += 1
    print(ans)

if '__main__' == __name__:
    resolve()