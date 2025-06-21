n = int(input())
w = list(input() for _ in range(n))
p = w[0][0]

if len(w) != len(set(w)):
    ans = 'No'
else:
    for i in w:
        if i[0] != p:
            ans = 'No'
            break
        else:
            p = i[-1]
    else:
        ans = 'Yes'

print(ans)
