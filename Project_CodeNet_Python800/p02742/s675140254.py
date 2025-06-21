#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import math

def get_num_of_reachable(H, W):
    if H == 1 or W == 1: return 1
    else: return math.ceil((H*W)/2)

def main():
    H, W = map(int, input().split())
    print(get_num_of_reachable(H, W))

if __name__ == "__main__":
    try:
        assert get_num_of_reachable(4, 5) == 10
        assert get_num_of_reachable(7, 3) == 11
        assert get_num_of_reachable(1000000000, 1000000000) == 500000000000000000
    except:
        import traceback
        traceback.print_exc()
        exit()
    main()
