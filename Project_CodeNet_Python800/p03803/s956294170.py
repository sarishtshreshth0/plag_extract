# A - One Card Poker
def main():
    a, b = map(int, input().split())

    if a == b:
        print('Draw')
    elif a == 1 and b != 1:
        print('Alice')
    elif a != 1 and b == 1:
        print('Bob')
    elif a > b:
        print('Alice')
    else:
        print('Bob')
  
        
if __name__ == '__main__':
    main()