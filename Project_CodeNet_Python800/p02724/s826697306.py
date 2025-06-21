def main():
    X = int(input())
    fh = X // 500
    X = X-fh*500
    fv = X//5

    print(fh*1000+fv*5)


main()
