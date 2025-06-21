#One Card Poker
def ABC_54_A():
    A,B = map(int, input().split())
    
    if A == 13 and B == 1:
        print('Bob')
    elif A == 1 and B == 13:
        print('Alice')
    elif A == B:
        print('Draw')
    elif A > B:
        print('Alice')
    else:
        print('Bob')


if __name__ == '__main__':

    ABC_54_A()