# -*- coding: utf-8 -*-
A, B = map(int, input().split())
S = input()
for i in range(len(S)):
    if i<A:
        if S[i].isdigit():
            pass
        else:
            print("No")
            break
    elif i==A:
        if S[i]!="-":
            print("No")
            break
    else:
        if S[i].isdigit():
            pass
        else:
            print("No")
            break
else:
    print("Yes")
