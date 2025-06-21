# -*- coding: utf-8 -*-
def main():
    h,w = map(int, input().split())
    if h == 1 or w == 1:
        print(1)
        return
    if h*w %2 == 0:
        print(int(h*w/2))
    else:
        print(int((h*w+1)/2))
    return


if __name__ == '__main__':
    main()