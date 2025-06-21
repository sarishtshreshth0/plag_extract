n = int(input())
word = []
for i in range(n) :
    word.append(input())
for i in range(1,n) :
    if word[i][0] != word[i-1][len(word[i-1]) - 1] :
        print("No")
        break
    if word[i] in word[:i] :
        print("No")
        break
else :
    print("Yes")
