N = int(input())
S = input()

need_left = 0
pointer = 0
for i in range(len(S)):
    if S[i] == '(':
        pointer += 1
    else:
        if pointer == 0:
            need_left += 1
        else:
            pointer -= 1
need_right = pointer

res = "(" * need_left + S + ")" * need_right
print(res)