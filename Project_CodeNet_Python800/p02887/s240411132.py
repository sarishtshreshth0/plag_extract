import re

N = int(input())
S = input()

result = ''

for i in range(len(S)):
    if i == len(S) - 1:
        result += S[i]
    elif S[i] != S[i+1]:
        result += S[i]

print(len(result))
