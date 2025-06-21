#!/usr/bin/env python3

import math
from decimal import *

def main():
    h,w = map(int, input().split())
    if h == 1:
        print(1)
        exit()
    elif w ==1:
        print(1)
        exit()
    else:
        print(math.ceil(h*w/2))

if __name__ == '__main__':
    main()