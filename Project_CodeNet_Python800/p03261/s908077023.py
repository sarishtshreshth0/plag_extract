N = int(input())
a = [input()]
for i in range(N-1):
    w = input()
    if not w in a and a[-1][-1] == w[0]:
        a.append(w)
    else:
        print("No")
        break
else:
    print("Yes")