#!/usr/bin/env python3

a, b, c = [int(x) for x in input().split()]
print("Yes" if a <= c <= b or b <= c <= a else "No")
