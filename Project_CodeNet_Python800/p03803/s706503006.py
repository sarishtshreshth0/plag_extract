def main():
    a,b = (int(x) for x in input().split())
    if a == b: print('Draw')
    elif (a < b and a != 1) or b == 1 : print('Bob')
    else: print('Alice')

if __name__ == '__main__':
    main()