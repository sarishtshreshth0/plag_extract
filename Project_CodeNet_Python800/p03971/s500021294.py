#!/usr/bin/env python3
n, a, b = map(int, input().split())
s = input()

cl = 0
clmax = a + b
wlrank = 0

for i in s:
    if i == "a":
        if cl < clmax:
            print("Yes")
            cl += 1
        else:
            print("No")

    elif i == "b":
        if cl < clmax:
            if wlrank < b:
                print("Yes")
                cl += 1
                wlrank += 1
            else:
                print("No")
        else:
            print("No") 
    else:
        print("No")
