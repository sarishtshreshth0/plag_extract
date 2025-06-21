#!/usr/bin/env python3

N,A,B= [int(x) for x in input().split(" ")]
S = input()

p = 0
p_b = 0
for i, x in enumerate(S):
    if x == 'a':
        if p < A + B:
            p += 1
            print("Yes")
        else:
            print("No")
    elif x == 'b':
        p_b += 1
        if p < A + B and p_b <= B:
            p += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    
