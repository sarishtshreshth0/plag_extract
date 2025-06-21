# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:05:25 2017

@author: taichiNakamura
"""

S = input()

def main(S):
    if len(S) < 4:
        return 'No'
    if S[:4] == 'YAKI':
        return 'Yes'
    else:
        return 'No'

print(main(S))