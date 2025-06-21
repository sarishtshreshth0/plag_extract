# -*- coding: utf-8 -*-

def main():
    
    A, B = map(int, input().split())

    if A == 1 and B != 1:
        ans = 'Alice'
    
    elif A != 1 and B == 1:
        ans = 'Bob'
    
    elif A == 1 and B == 1:
        ans = 'Draw'

    elif A > B:
        ans = 'Alice'

    elif A < B:
        ans = 'Bob'
    
    elif A == B:
        ans = 'Draw'

    print(ans)


if __name__ == "__main__":
    main()