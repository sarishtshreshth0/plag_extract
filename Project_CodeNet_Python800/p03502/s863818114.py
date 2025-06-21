def main():
    n = input()
    w = 0
    for i in n:
        w += int(i)
    if int(n)%w == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
