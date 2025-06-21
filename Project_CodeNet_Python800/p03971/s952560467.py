#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-25 13:44:41 +0900
# LastModified: 2020-06-25 13:54:38 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, a, b = map(int, input().split())
    s = input()
    win = 0
    foreign = 0
    for i in range(n):
        if s[i] == 'a' and win < a+b:
            win += 1
            print("Yes")

        elif s[i] == 'b' and win < a+b and foreign < b:
            win += 1
            foreign += 1
            print("Yes")
        else:
            print("No")
            


if __name__ == "__main__":
    main()
