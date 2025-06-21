#! env python
# -*- coding: utf-8 -*-

import os
import sys


# ac_py.main
# Date: 2020/06/14
# Filename: main 
# Author: acto_mini

def main():
    A, B, C, D = map(int, input().split())

    if B > C:
        if A <= C <= B and A <= D <= B:
            print(D - C)
        elif A <= D <= B and A >= C:
            print(D - A)
        elif A <= C <= B and D >= B:
            print(B - C)
        elif C <= A and B <= D:
            print(B - A)
        else:
            print(0)
    else:
        print(0)
    return


if __name__ == '__main__':
    main()
