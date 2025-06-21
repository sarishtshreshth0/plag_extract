def resolve():
    S = input()
    zero = 0
    one = 0
    for i in range(len(S)):
        if i%2 == 0 and S[i] != "0" or i%2 == 1 and S[i] != "1":
            zero += 1
        elif i%2 == 0 and S[i] != "1" or i%2 == 1 and S[i] != "0":
            one += 1
    print(min(one, zero))
resolve()