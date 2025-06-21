N = int(input())
ans = 'Yes'
a = set()
pre = ''
for i in range(N):
    word = input()
    if not word in a and (pre == word[0] or pre == '') and ans == 'Yes':
        ans = 'Yes'
        a.add(word)
        pre = word[-1]
    else:
        ans = 'No'
print(ans)
