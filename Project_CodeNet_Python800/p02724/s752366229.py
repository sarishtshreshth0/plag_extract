def main():
    x = int(input())
    c = 0

    c += 1000 * (x//500)
    x -= 500 * (x//500)

    c += 5 * (x//5)
    print(c)
    return
main()
