
def hoge(S):
    cum = 0
    mi = 0
    for s in S:
        cum += 1 if s == '(' else -1
        mi = min(mi, cum)
    return (-mi, cum - mi)

N = int(input())
S = input()

l, r = hoge(S)
print('(' * l + S + ')' * r)