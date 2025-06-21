N = int(input())

used_word = []
cher = ""
for _ in range(N):
    W = input()
    if not cher:
        used_word.append(W)
        cher = W[-1]
    else:
        if W[0] == cher and W not in used_word:
            used_word.append(W)
            cher = W[-1]
        else:
            print("No")
            break
else:
    print("Yes")