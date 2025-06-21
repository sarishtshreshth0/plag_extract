# -*- coding:utf-8 -*-
n,a,b = map(int,input().split())
member_list = list(input())

thr_dom = a+b
thr_nat = b
pass_num = 0
pass_nat = 0

for member in member_list:
    if member == 'a':
        if pass_num < thr_dom:
            print("Yes")
            pass_num += 1
        else:
            print("No")
    elif member == "b":
        if pass_num < thr_dom and pass_nat < thr_nat:
            print("Yes")
            pass_num += 1
            pass_nat += 1
        else:
            print("No")
    else:
        print("No")
