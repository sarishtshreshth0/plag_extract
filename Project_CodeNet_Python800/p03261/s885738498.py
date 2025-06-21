n = int(input())
w = input()
words=[]

ans = "Yes"

words.append(w)

for i in range(1,n):
    w = input()
    if w not in words:
        if words[-1][-1]==w[0]:
            words.append(w)
            continue
        else:
            ans = "No"
            break
    else:
        ans = "No"
        break
print(ans)

