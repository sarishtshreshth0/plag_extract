N = int(input())

words = []
ans = "Yes"
for count in range(N):
    word = input()
    if count == 0:
        words.append(word)
        next = word[-1]
        continue
    if next != word[0]:
        ans = "No"
    if words.count(word) == 1:
        ans = "No"
    words.append(word)
    next = word[-1]


print(ans)