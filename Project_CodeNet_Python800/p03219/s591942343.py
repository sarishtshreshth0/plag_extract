def main():
    from sys import stdin
    r = stdin.readline()[:-1]
    #r = stdin.readlines()

    x, y = map(int, r.split())
    print(x+y//2)
   
if __name__ == '__main__':
    main()

