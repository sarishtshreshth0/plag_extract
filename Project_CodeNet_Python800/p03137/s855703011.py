# -*- coding: utf-8 -*-

import sys

def main():
    input = sys.stdin.readline
    n,m = map(int, input().split())
    x_list = list(map(int, input().split()))
    if n >= m:
        print(0)
        exit(0)
    sabun_list = []
    x_list.sort()
    for i,x in  enumerate(x_list):
        if i == 0:
            continue
        sabun_list.append(x - x_list[i-1])
    result = 0
    sum_max_sabun = 0
    sabun_list.sort(reverse=True)
    sum_max_sabun = sum(sabun_list[:n-1])
    
    result = (x_list[-1] - x_list[0]) - sum_max_sabun

    print(result)

    return


if __name__ == '__main__':
    main()