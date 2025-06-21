#!/usr/bin/env python3

N = int(input())
S = input()

left = [] 

for i, s in enumerate(S):
    if s == "(":
        left.append("(")
    else:
        if len(left) > 0:
            left.pop()
        else:
            S = "(" + S

for _ in range(len(left)):
    S += ")"

print(S)