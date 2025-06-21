word = input()

res = 0
colour = 0
for s in word:
    if colour % 2 != int(s):
        res += 1
    colour += 1
if len(word) // 2 < res:
    res = len(word) - res

print(res)
