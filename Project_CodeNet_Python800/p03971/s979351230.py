n, a, b = map(int, input().split())
s = input()

cnt_t = 0
cnt_f = 0
for i in range(n):
    if s[i] == "a" and cnt_t < a+b:
        print("Yes")
        cnt_t += 1
    elif s[i] == "b" and cnt_t < a+b and cnt_f < b:
        print("Yes")
        cnt_t += 1
        cnt_f += 1
    else:
        print("No")