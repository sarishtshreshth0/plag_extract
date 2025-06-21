#!/usr/bin/env python3
# スペース区切りの整数の入力
A, B = map(int, input().split())
S = input()

index = S.find("-")
if S.count("-") != 1:
    print("No")
    exit(0)
if index == -1:
    print("No")
    exit(0)
if len(S[:index]) != A:
    print("No")
    exit(0)
if len(S[index+1:]) != B:
    print("No")
    exit(0)

print("Yes")
