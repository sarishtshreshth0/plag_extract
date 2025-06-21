def resolve():
    X = int(input())
    ans = (X//500)*1000
    ans += ((X%500)//5)*5
    print(ans)


if '__main__' == __name__:
    resolve()