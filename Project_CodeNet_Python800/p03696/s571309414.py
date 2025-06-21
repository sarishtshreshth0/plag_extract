N = int(input())
S = input()

front_not_close = 0
end_not_close = 0

for s in list(S):
    if s == '(':
        front_not_close += 1
    else:
        if front_not_close > 0:
            front_not_close -= 1
        else:
            end_not_close += 1


for i in range(end_not_close):
    S = '(' + S

for i in range(front_not_close):
    S = S + ')'

print(S)
